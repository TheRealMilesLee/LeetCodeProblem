#!/usr/bin/env python3
"""
Large-scale Palindrome Query Benchmark

Algorithms:
    1. Manacher preprocessing: O(N)
    2. Range palindrome query: O(1)
    3. Single-thread benchmark
    4. Multi-thread benchmark
    5. Multi-process benchmark

Example:
    python palindrome_benchmark.py
    python palindrome_benchmark.py --size 1000000 --queries 100000
    python palindrome_benchmark.py --size 5000000 --queries 500000 --mode process
"""

import argparse
import random
import os
import time

from array import array
from concurrent.futures import (
    ThreadPoolExecutor,
    ProcessPoolExecutor,
)

# ============================================================
# 1. Manacher Algorithm
# ============================================================


class Manacher:

  def __init__(self, s: str):

    self.n = len(s)

    n = self.n

    # Odd palindrome radius
    self.d1 = array("I", [0]) * n

    left, right = 0, -1

    for i in range(n):

      if i > right:
        k = 1
      else:
        k = min(self.d1[left + right - i], right - i + 1)

      while (i - k >= 0 and i + k < n and s[i - k] == s[i + k]):
        k += 1

      self.d1[i] = k

      if i + k - 1 > right:
        left = i - k + 1
        right = i + k - 1

    # Even palindrome radius
    self.d2 = array("I", [0]) * n

    left, right = 0, -1

    for i in range(n):

      if i > right:
        k = 0
      else:
        k = min(self.d2[left + right - i + 1], right - i + 1)

      while (i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]):
        k += 1

      self.d2[i] = k

      if i + k - 1 > right:
        left = i - k
        right = i + k - 1

  def is_palindrome(self, l: int, r: int) -> bool:
    """
        Check substring s[l:r].
        Uses half-open interval [l, r).
        """

    if not (0 <= l <= r <= self.n):
      raise ValueError("Invalid range")

    length = r - l

    if length <= 1:
      return True

    if length % 2 == 1:

      center = (l + r - 1) // 2

      return (self.d1[center] >= length // 2 + 1)

    else:

      center = (l + r) // 2

      return (self.d2[center] >= length // 2)


# ============================================================
# 2. Large Text Generator
# ============================================================


def generate_book(size: int, seed: int = 42):

  rng = random.Random(seed)

  print(f"[Generator] Creating {size:,} characters...")

  # Generate random lowercase text
  book = bytearray(rng.choices(range(97, 123), k=size))

  # Plant known palindrome segments
  palindrome_spans = []

  palindrome_count = min(1000, size // 101)

  spacing = max(101, size // max(1, palindrome_count))

  for i in range(palindrome_count):

    start = i * spacing

    if start + 101 > size:
      break

    # Generate a random 50-character half
    half = bytes(rng.choices(range(97, 123), k=50))

    # Construct a 101-character palindrome
    palindrome = half + bytes([rng.randrange(97, 123)]) + half[::-1]

    book[start:start + 101] = palindrome

    palindrome_spans.append((start, start + 101))

  print(f"[Generator] Planted {len(palindrome_spans):,} palindromes")

  return book.decode("ascii"), palindrome_spans


# ============================================================
# 3. Query Generator
# ============================================================


def generate_queries(book: str,
                     palindrome_spans: list,
                     query_count: int,
                     seed: int = 123):

  rng = random.Random(seed)

  n = len(book)

  queries = []

  positive_count = query_count // 2

  # Known positive queries
  for i in range(positive_count):

    l, r = palindrome_spans[i % len(palindrome_spans)]

    queries.append((l, r, True))

  # Guaranteed negative queries
  while len(queries) < query_count:

    length = rng.randint(100, min(500, n))

    l = rng.randint(0, n - length)

    r = l + length

    # Different first and last characters guarantee
    # that this substring is NOT a palindrome.
    if book[l] != book[r - 1]:

      queries.append((l, r, False))

  rng.shuffle(queries)

  return queries


# ============================================================
# 4. Shared Worker State
# ============================================================

_WORKER_INDEX = None


def init_worker(d1, d2, n):

  global _WORKER_INDEX

  # Each process receives the precomputed arrays once.
  _WORKER_INDEX = Manacher.__new__(Manacher)

  _WORKER_INDEX.n = n
  _WORKER_INDEX.d1 = d1
  _WORKER_INDEX.d2 = d2


def check_chunk(chunk):

  true_count = 0
  errors = 0

  for l, r, expected in chunk:

    assert _WORKER_INDEX is not None
    result = _WORKER_INDEX.is_palindrome(l, r)

    if result:
      true_count += 1

    if result != expected:
      errors += 1

  return true_count, errors


# ============================================================
# 5. Benchmark Utilities
# ============================================================


def split_chunks(items, chunk_size):

  return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]


def benchmark_serial(index, queries):

  start = time.perf_counter()

  true_count = 0
  errors = 0

  for l, r, expected in queries:

    result = index.is_palindrome(l, r)

    if result:
      true_count += 1

    if result != expected:
      errors += 1

  elapsed = time.perf_counter() - start

  return elapsed, true_count, errors


def benchmark_parallel(index, queries, workers, mode="thread"):

  global _WORKER_INDEX

  _WORKER_INDEX = index

  chunk_size = max(1, len(queries) // (workers * 4))

  chunks = split_chunks(queries, chunk_size)

  start = time.perf_counter()

  if mode == "thread":

    with ThreadPoolExecutor(max_workers=workers) as executor:

      results = list(executor.map(check_chunk, chunks))

  elif mode == "process":

    with ProcessPoolExecutor(max_workers=workers,
                             initializer=init_worker,
                             initargs=(index.d1, index.d2,
                                       index.n)) as executor:

      results = list(executor.map(check_chunk, chunks))

  else:
    raise ValueError("Unknown execution mode")

  elapsed = time.perf_counter() - start

  true_count = sum(x[0] for x in results)
  errors = sum(x[1] for x in results)

  return elapsed, true_count, errors


# ============================================================
# 6. Main
# ============================================================


def main():

  parser = argparse.ArgumentParser(
      description="Large-scale Palindrome Benchmark")

  parser.add_argument("--size", type=int, default=1_000_000_000)

  parser.add_argument("--queries", type=int, default=100_000_000)

  parser.add_argument("--workers",
                      type=int,
                      default=min(4,
                                  os.cpu_count() or 1))

  parser.add_argument("--mode",
                      choices=["all", "serial", "thread", "process"],
                      default="all")

  args = parser.parse_args()

  if args.size < 101 or args.queries < 1 or args.workers < 1:
    parser.error("Invalid size, queries, or workers")

  print("=" * 60)
  print(" LARGE-SCALE PALINDROME BENCHMARK")
  print("=" * 60)

  print(f"CPU cores : {os.cpu_count()}")
  print(f"Text size : {args.size:,}")
  print(f"Queries   : {args.queries:,}")
  print(f"Workers   : {args.workers}")
  print()

  # Generate text
  book, palindrome_spans = generate_book(args.size)

  # Generate queries
  queries = generate_queries(book, palindrome_spans, args.queries)

  print()

  # Manacher preprocessing
  print("[Manacher] Preprocessing...")

  start = time.perf_counter()

  index = Manacher(book)

  preprocess_time = time.perf_counter() - start

  print(f"[Manacher] Completed in "
        f"{preprocess_time:.4f}s")

  print()

  results = {}

  # Single-thread benchmark
  if args.mode in ("all", "serial"):

    print("[Benchmark] Single Thread")

    elapsed, count, errors = benchmark_serial(index, queries)

    results["serial"] = elapsed

    print(f"Time   : {elapsed:.4f}s")
    print(f"QPS    : {len(queries) / elapsed:,.0f}")
    print(f"True   : {count:,}")
    print(f"Errors : {errors:,}")
    print()

  # Multi-thread benchmark
  if args.mode in ("all", "thread"):

    print("[Benchmark] Multi Thread")

    elapsed, count, errors = benchmark_parallel(index,
                                                queries,
                                                args.workers,
                                                mode="thread")

    results["thread"] = elapsed

    print(f"Time   : {elapsed:.4f}s")
    print(f"QPS    : {len(queries) / elapsed:,.0f}")
    print(f"True   : {count:,}")
    print(f"Errors : {errors:,}")
    print()

  # Multi-process benchmark
  if args.mode in ("all", "process"):

    print("[Benchmark] Multi Process")

    elapsed, count, errors = benchmark_parallel(index,
                                                queries,
                                                args.workers,
                                                mode="process")

    results["process"] = elapsed

    print(f"Time   : {elapsed:.4f}s")
    print(f"QPS    : {len(queries) / elapsed:,.0f}")
    print(f"True   : {count:,}")
    print(f"Errors : {errors:,}")
    print()

  # Summary
  print("=" * 60)
  print(" SUMMARY")
  print("=" * 60)

  print(f"Preprocessing : {preprocess_time:.4f}s")

  for name, elapsed in results.items():

    print(f"{name:12s}: "
          f"{elapsed:.4f}s")

  if "serial" in results:

    baseline = results["serial"]

    for name, elapsed in results.items():

      if name != "serial":

        speedup = baseline / elapsed

        print(f"{name} speedup: "
              f"{speedup:.2f}x")

  print("=" * 60)


if __name__ == "__main__":
  main()
