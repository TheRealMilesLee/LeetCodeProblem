# Large-Scale Palindrome Benchmark

C++20 / Apple Clang / Makefile / POSIX `mmap`.

## What this first version does

1. Creates a deterministic ASCII dataset in `data/text.bin`.
2. Generates text in parallel, then plants known odd-length palindromes.
3. Builds exact Manacher odd/even radius indexes in memory-mapped files.
4. Executes queries in parallel without materializing a giant query array.
5. Writes a CSV summary to `results/benchmark.csv`.

**Important:** Manacher preprocessing is intentionally serial in this version. Standard Manacher has cross-position dependencies; splitting the input into independent chunks and concatenating their radii is not correct for unlimited-length palindrome queries.

## Requirements

- macOS on Apple Silicon
- Xcode Command Line Tools (`xcode-select --install`)
- `clang++`, `make`

No CMake and no third-party dependencies.

## Build

```bash
make
```

## Smoke test first

```bash
./build/palindrome_benchmark \
  --size 1000000 \
  --queries 100000 \
  --threads 4
```

Then scale up:

```bash
./build/palindrome_benchmark --size 100000000 --queries 1000000 --threads 10
./build/palindrome_benchmark --size 500000000 --queries 5000000 --threads 10
```

Only after those succeed, run 1B:

```bash
./build/palindrome_benchmark --size 1000000000 --queries 10000000 --threads 10
```

The default `make run-1b` target is provided, but do not run it before the smaller stages have completed successfully.

## Files

- `data/text.bin`: generated input, 1 byte per character.
- `data/manacher_odd.bin`: odd-radius index, uint32 per character.
- `data/manacher_even.bin`: even-radius index, uint32 per character.
- `results/benchmark.csv`: run summary.

At 1B characters, the three data files total approximately 9 GB (decimal), excluding filesystem overhead.

## Query semantics

All query intervals are half-open: `[left, right)`.
The benchmark uses two classes:

- Positive: selects one of the planted known palindrome intervals.
- Negative: chooses a range whose first and last characters differ. Such a range is guaranteed not to be a palindrome.

This gives a deterministic 50/50 positive/negative workload and a direct correctness check.

## Memory and storage warnings

- `mmap` avoids allocating one giant C++ heap object, but mapped pages still use physical memory and can contribute to memory pressure.
- The index build writes 8 GB of radius data at 1B characters. On a 16 GB Mac, watch Activity Monitor's Memory Pressure and Swap Used.
- Keep substantial free SSD space. Do not run multiple copies simultaneously.
- If Memory Pressure turns yellow/red or Swap grows rapidly, stop with Ctrl-C.
- The current implementation calls `msync(MS_SYNC)` at phase boundaries, so the phase timings include persistence cost.

## Notes on performance

- Generation and query execution are parallel.
- Manacher preprocessing is serial and exact.
- Query generation is performed on the fly per worker; there is no 10M-query allocation.
- `Peak RSS` is process peak resident memory from `getrusage`; it is not a complete measure of macOS file-cache pressure.
- The reported total includes file creation, generation, index build, and query execution.

## Clean generated data

```bash
rm -f data/text.bin data/manacher_odd.bin data/manacher_even.bin
```

Use `make clean` only to remove the compiled binary.
