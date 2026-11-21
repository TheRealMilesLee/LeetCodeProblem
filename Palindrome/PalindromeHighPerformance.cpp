#include <algorithm>
#include <array>
#include <atomic>
#include <cerrno>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstring>
#include <cstdio>
#include <fcntl.h>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <memory>
#include <mutex>
#include <random>
#include <stdexcept>
#include <string>
#include <string_view>
#include <sys/mman.h>
#include <sys/resource.h>
#include <sys/stat.h>
#include <thread>
#include <chrono>
#include <unistd.h>
#include <vector>

namespace fs = std::filesystem;
using Clock = std::chrono::steady_clock;

struct Config
{
  uint64_t size = 1'000'000;
  uint64_t queries = 100'000;
  unsigned threads = std::max(1u, std::thread::hardware_concurrency());
  uint64_t seed = 20261121;
  fs::path dir = "data";
  uint64_t planted = 1000;
  uint32_t planted_length = 101;
};

static void usage(const char* argv0)
{
  std::cout
      << "Usage: " << argv0 << " [options]\n"
      << "  --size N       Text size in characters (default 1000000)\n"
      << "  --queries N    Number of benchmark queries (default 100000)\n"
      << "  --threads N    Worker threads (default hardware concurrency)\n"
      << "  --seed N       Reproducible seed (default 20261121)\n"
      << "  --dir PATH     Data directory (default data)\n"
      << "  --help         Show this help\n\n"
      << "Example:\n"
      << "  " << argv0
      << " --size 1000000000 --queries 10000000 --threads 4\n";
}

static uint64_t parse_u64(const std::string& s, const char* name)
{
  size_t used = 0;
  unsigned long long v = 0;
  try
  {
    v = std::stoull(s, &used);
  }
  catch (...)
  {
    throw std::runtime_error(std::string("Invalid ") + name + ": " + s);
  }
  if (used != s.size())
    throw std::runtime_error(std::string("Invalid ") + name + ": " + s);
  return static_cast<uint64_t>(v);
}

static Config parse_args(int argc, char** argv)
{
  Config c;
  for (int i = 1; i < argc; ++i)
  {
    const std::string a = argv[i];
    auto value = [&](const char* name) -> std::string
    {
      if (i + 1 >= argc)
        throw std::runtime_error(std::string("Missing value for ") + name);
      return argv[++i];
    };
    if (a == "--size")
      c.size = parse_u64(value("--size"), "size");
    else if (a == "--queries")
      c.queries = parse_u64(value("--queries"), "queries");
    else if (a == "--threads")
      c.threads =
          static_cast<unsigned>(parse_u64(value("--threads"), "threads"));
    else if (a == "--seed")
      c.seed = parse_u64(value("--seed"), "seed");
    else if (a == "--dir")
      c.dir = value("--dir");
    else if (a == "--help" || a == "-h")
    {
      usage(argv[0]);
      std::exit(0);
    }
    else
      throw std::runtime_error("Unknown argument: " + a);
  }
  if (c.size < c.planted_length + 2)
    throw std::runtime_error("--size must be at least 103");
  if (c.size > std::numeric_limits<uint32_t>::max())
    throw std::runtime_error(
        "This build uses uint32_t indices; --size must be <= 4,294,967,295");
  if (c.threads == 0) throw std::runtime_error("--threads must be >= 1");
  if (c.threads > 64)
    throw std::runtime_error("--threads must be <= 64 for this benchmark");
  if (c.queries == 0) throw std::runtime_error("--queries must be >= 1");
  return c;
}

class MappedFile
{
public:
  MappedFile(const fs::path& path, uint64_t bytes, bool create)
    : path_(path), bytes_(bytes)
  {
    if (bytes == 0
        || bytes > static_cast<uint64_t>(std::numeric_limits<off_t>::max()))
      throw std::runtime_error("Invalid mapping size for " + path.string());
    int flags = create ? (O_RDWR | O_CREAT | O_TRUNC) : O_RDWR;
    fd_ = ::open(path.c_str(), flags, 0644);
    if (fd_ < 0)
      throw std::runtime_error("open failed for " + path.string() + ": "
                               + std::strerror(errno));
    if (create && ::ftruncate(fd_, static_cast<off_t>(bytes)) != 0)
    {
      const std::string e = std::strerror(errno);
      ::close(fd_);
      fd_ = -1;
      throw std::runtime_error("ftruncate failed for " + path.string() + ": "
                               + e);
    }
    struct stat st{};
    if (::fstat(fd_, &st) != 0 || static_cast<uint64_t>(st.st_size) < bytes)
    {
      ::close(fd_);
      fd_ = -1;
      throw std::runtime_error("File is smaller than expected: "
                               + path.string());
    }
    void* p = ::mmap(nullptr,
                     static_cast<size_t>(bytes),
                     PROT_READ | PROT_WRITE,
                     MAP_SHARED,
                     fd_,
                     0);
    if (p == MAP_FAILED)
    {
      const std::string e = std::strerror(errno);
      ::close(fd_);
      fd_ = -1;
      throw std::runtime_error("mmap failed for " + path.string() + ": " + e);
    }
    data_ = static_cast<uint8_t*>(p);
#ifdef MADV_SEQUENTIAL
    (void) ::madvise(data_, static_cast<size_t>(bytes), MADV_SEQUENTIAL);
#endif
  }
  ~MappedFile()
  {
    if (data_)
    {
      (void) ::msync(data_, static_cast<size_t>(bytes_), MS_SYNC);
      ::munmap(data_, static_cast<size_t>(bytes_));
    }
    if (fd_ >= 0) ::close(fd_);
  }
  MappedFile(const MappedFile&) = delete;
  MappedFile& operator=(const MappedFile&) = delete;
  uint8_t* bytes()
  {
    return data_;
  }
  const uint8_t* bytes() const
  {
    return data_;
  }
  uint64_t size() const
  {
    return bytes_;
  }
  void sync()
  {
    if (::msync(data_, static_cast<size_t>(bytes_), MS_SYNC) != 0)
      throw std::runtime_error("msync failed for " + path_.string() + ": "
                               + std::strerror(errno));
  }

private:
  fs::path path_;
  uint64_t bytes_ = 0;
  int fd_ = -1;
  uint8_t* data_ = nullptr;
};

struct KnownPalindrome
{
  uint64_t start;
  uint32_t length;
};

static double seconds_since(Clock::time_point start)
{
  return std::chrono::duration<double>(Clock::now() - start).count();
}

static void print_stage(const std::string& label, double seconds)
{
  std::cout << std::left << std::setw(28) << label << std::right << std::fixed
            << std::setprecision(4) << seconds << " s\n";
}

static void generate_text(MappedFile& text,
                          const Config& c,
                          std::vector<KnownPalindrome>& planted)
{
  std::cout << "\n[1/4] PARALLEL DATA GENERATION\n";
  const uint64_t n = c.size;
  const unsigned workers =
      static_cast<unsigned>(std::min<uint64_t>(c.threads, n));
  const auto start = Clock::now();
  std::vector<std::thread> pool;
  pool.reserve(workers);
  std::atomic<uint64_t> completed{ 0 };

  for (unsigned tid = 0; tid < workers; ++tid)
  {
    const uint64_t begin = n * tid / workers;
    const uint64_t end = n * (tid + 1) / workers;
    pool.emplace_back(
        [&, tid, begin, end]
        {
          std::mt19937_64 rng(c.seed ^ (0x9E3779B97F4A7C15ULL * (tid + 1)));
          std::uniform_int_distribution<unsigned> dist(0, 25);
          uint8_t* out = text.bytes();
          constexpr uint64_t block = 8ULL * 1024 * 1024;
          for (uint64_t chunk = begin; chunk < end; chunk += block)
          {
            const uint64_t stop = std::min(end, chunk + block);
            for (uint64_t i = chunk; i < stop; ++i)
              out[i] = static_cast<uint8_t>('a' + dist(rng));
            completed.fetch_add(stop - chunk, std::memory_order_relaxed);
          }
        });
  }
  uint64_t last_reported = 0;
  while (completed.load(std::memory_order_relaxed) < n)
  {
    std::this_thread::sleep_for(std::chrono::seconds(1));
    const uint64_t done = completed.load(std::memory_order_relaxed);
    if (done != last_reported)
    {
      std::cout << "  Generated: " << done << " / " << n << " bytes ("
                << std::fixed << std::setprecision(1)
                << (100.0 * static_cast<double>(done)
                    / static_cast<double>(n))
                << "%)\n";
      last_reported = done;
    }
  }
  for (auto& t : pool) t.join();

  planted.clear();
  planted.reserve(static_cast<size_t>(c.planted));
  std::mt19937_64 prng(c.seed ^ 0xD1B54A32D192ED03ULL);
  std::uniform_int_distribution<unsigned> char_dist(0, 25);
  // Place deterministic, non-overlapping odd palindromes at evenly spaced offsets.
  const uint64_t slots = std::max<uint64_t>(1, n / (c.planted + 1));
  for (uint64_t k = 0; k < c.planted; ++k)
  {
    const uint64_t start_pos = (k + 1) * slots;
    if (start_pos + c.planted_length >= n) break;
    const uint32_t half = c.planted_length / 2;
    for (uint32_t j = 0; j < half; ++j)
    {
      const uint8_t ch = static_cast<uint8_t>('a' + char_dist(prng));
      text.bytes()[start_pos + j] = ch;
      text.bytes()[start_pos + c.planted_length - 1 - j] = ch;
    }
    text.bytes()[start_pos + half] =
        static_cast<uint8_t>('a' + char_dist(prng));
    planted.push_back({ start_pos, c.planted_length });
  }
  text.sync();
  const double elapsed = seconds_since(start);
  print_stage("Generation + planting", elapsed);
  std::cout << "  Workers: " << workers << " | Bytes: " << completed.load()
            << " | Planted palindromes: " << planted.size() << "\n";
  std::cout << "  Throughput: " << std::fixed << std::setprecision(2)
            << (static_cast<double>(n) / (1024.0 * 1024.0) / elapsed)
            << " MiB/s\n";
}

struct ManacherIndex
{
  uint32_t* odd = nullptr;
  uint32_t* even = nullptr;
  uint64_t n = 0;
};

static void build_manacher(const MappedFile& text,
                           MappedFile& odd_file,
                           MappedFile& even_file,
                           uint64_t n)
{
  std::cout << "\n[2/4] MANACHER PREPROCESSING (exact, serial)\n";
  auto* d1 = reinterpret_cast<uint32_t*>(odd_file.bytes());
  auto* d2 = reinterpret_cast<uint32_t*>(even_file.bytes());
  const uint8_t* s = text.bytes();
  const auto start = Clock::now();

  int64_t left = 0, right = -1;
  for (int64_t i = 0; i < static_cast<int64_t>(n); ++i)
  {
    int64_t k = (i > right)
        ? 1
        : std::min<int64_t>(d1[left + right - i], right - i + 1);
    while (i - k >= 0 && i + k < static_cast<int64_t>(n)
           && s[i - k] == s[i + k])
      ++k;
    d1[i] = static_cast<uint32_t>(k);
    if (i + k - 1 > right)
    {
      left = i - k + 1;
      right = i + k - 1;
    }
    if ((i + 1) % 100'000'000LL == 0)
      std::cout << "  Odd radii: " << (i + 1) << " / " << n << "\n";
  }

  left = 0;
  right = -1;
  for (int64_t i = 0; i < static_cast<int64_t>(n); ++i)
  {
    int64_t k = (i > right)
        ? 0
        : std::min<int64_t>(d2[left + right - i + 1], right - i + 1);
    while (i - k - 1 >= 0 && i + k < static_cast<int64_t>(n)
           && s[i - k - 1] == s[i + k])
      ++k;
    d2[i] = static_cast<uint32_t>(k);
    if (i + k - 1 > right)
    {
      left = i - k;
      right = i + k - 1;
    }
    if ((i + 1) % 100'000'000LL == 0)
      std::cout << "  Even radii: " << (i + 1) << " / " << n << "\n";
  }
  odd_file.sync();
  even_file.sync();
  print_stage("Manacher index build", seconds_since(start));
  std::cout << "  Index size: " << std::fixed << std::setprecision(2)
            << (16.0 * static_cast<double>(n) / (1024.0 * 1024.0 * 1024.0))
            << " GiB (odd + even)\n";
}

static inline bool is_palindrome(uint64_t l,
                                 uint64_t r,
                                 const uint32_t* d1,
                                 const uint32_t* d2)
{
  // Half-open interval [l, r).
  const uint64_t len = r - l;
  if (len <= 1) return true;
  if (len & 1ULL)
  {
    const uint64_t center = l + len / 2;
    return d1[center] >= (len / 2 + 1);
  }
  const uint64_t center = l + len / 2;
  return d2[center] >= (len / 2);
}

struct QueryStats
{
  uint64_t total = 0;
  uint64_t yes = 0;
  uint64_t no = 0;
  uint64_t errors = 0;
};

static void run_query_benchmark(const MappedFile& text,
                                const MappedFile& odd_file,
                                const MappedFile& even_file,
                                const Config& c,
                                const std::vector<KnownPalindrome>& planted)
{
  std::cout << "\n[3/4] PARALLEL QUERY BENCHMARK\n";
  const auto* d1 = reinterpret_cast<const uint32_t*>(odd_file.bytes());
  const auto* d2 = reinterpret_cast<const uint32_t*>(even_file.bytes());
  const uint8_t* s = text.bytes();
  const unsigned workers =
      static_cast<unsigned>(std::min<uint64_t>(c.threads, c.queries));
  std::vector<QueryStats> stats(workers);
  std::vector<std::thread> pool;
  pool.reserve(workers);
  const auto start = Clock::now();

  for (unsigned tid = 0; tid < workers; ++tid)
  {
    const uint64_t count =
        c.queries / workers + (tid < c.queries % workers ? 1 : 0);
    pool.emplace_back(
        [&, tid, count]
        {
          std::mt19937_64 rng(c.seed + 0x9E3779B97F4A7C15ULL * (tid + 17));
          std::uniform_int_distribution<uint64_t> pos_dist(0, c.size - 2);
          QueryStats local;
          for (uint64_t q = 0; q < count; ++q)
          {
            uint64_t l = 0, r = 0;
            bool expected = false;
            if ((q & 1ULL) == 0 && !planted.empty())
            {
              const auto& p = planted[rng() % planted.size()];
              l = p.start;
              r = p.start + p.length;
              expected = true;
            }
            else
            {
              // A string whose first and last bytes differ cannot be a palindrome.
              // This yields guaranteed negative queries without storing query objects.
              for (;;)
              {
                l = pos_dist(rng);
                const uint64_t max_len = c.size - l;
                const uint64_t upper = std::min<uint64_t>(max_len, 100'000);
                if (upper < 2) continue;
                std::uniform_int_distribution<uint64_t> local_len(2, upper);
                r = l + local_len(rng);
                if (s[l] != s[r - 1]) break;
              }
            }
            const bool actual = is_palindrome(l, r, d1, d2);
            ++local.total;
            if (actual)
              ++local.yes;
            else
              ++local.no;
            if (actual != expected) ++local.errors;
          }
          stats[tid] = local;
        });
  }
  for (auto& t : pool) t.join();
  const double elapsed = seconds_since(start);
  QueryStats total;
  for (const auto& x : stats)
  {
    total.total += x.total;
    total.yes += x.yes;
    total.no += x.no;
    total.errors += x.errors;
  }
  print_stage("Parallel query execution", elapsed);
  std::cout << "  Workers: " << workers << "\n"
            << "  Queries: " << total.total << "\n"
            << "  QPS: " << std::fixed << std::setprecision(0)
            << (static_cast<double>(total.total) / elapsed) << "\n"
            << "  True: " << total.yes << "\n"
            << "  False: " << total.no << "\n"
            << "  Errors: " << total.errors << "\n";
}

static uint64_t peak_rss_bytes()
{
  struct rusage usage{};
  if (getrusage(RUSAGE_SELF, &usage) != 0) return 0;
#if defined(__APPLE__)
  return static_cast<uint64_t>(usage.ru_maxrss);
#else
  return static_cast<uint64_t>(usage.ru_maxrss) * 1024ULL;
#endif
}

static void write_report(const Config& c,
                         double total_seconds,
                         const fs::path& result_path)
{
  const uint64_t rss = peak_rss_bytes();
  const bool needs_header =
      !fs::exists(result_path) || fs::file_size(result_path) == 0;
  std::ofstream out(result_path, std::ios::app);
  if (!out)
    throw std::runtime_error("Cannot write result file: "
                             + result_path.string());
  if (needs_header)
    out << "size,queries,threads,seed,total_seconds,peak_rss_bytes\n";
  out << c.size << ',' << c.queries << ',' << c.threads << ',' << c.seed
      << ',' << std::fixed << std::setprecision(6) << total_seconds << ','
      << rss << '\n';
  std::cout << "\n[4/4] SYSTEM SUMMARY\n"
            << "  Peak RSS (process): " << std::fixed << std::setprecision(2)
            << (static_cast<double>(rss) / (1024.0 * 1024.0 * 1024.0))
            << " GiB\n"
            << "  Result CSV: " << result_path << "\n";
}

int main(int argc, char** argv)
{
  try
  {
    const Config c = parse_args(argc, argv);
    fs::create_directories(c.dir);
    fs::create_directories("results");

    const fs::path text_path = c.dir / "text.bin";
    const fs::path odd_path = c.dir / "manacher_odd.bin";
    const fs::path even_path = c.dir / "manacher_even.bin";
    const uint64_t index_bytes = c.size * sizeof(uint32_t);

    std::cout
        << "============================================================\n"
        << " LARGE-SCALE PALINDROME BENCHMARK (C++20 / mmap)\n"
        << "============================================================\n"
        << "Text size : " << c.size << "\n"
        << "Queries   : " << c.queries << "\n"
        << "Threads   : " << c.threads << "\n"
        << "Seed      : " << c.seed << "\n"
        << "Data dir  : " << c.dir << "\n"
        << "Index     : exact Manacher (serial preprocessing)\n";

    const auto total_start = Clock::now();
    MappedFile text(text_path, c.size, true);
    std::vector<KnownPalindrome> planted;
    generate_text(text, c, planted);

    MappedFile odd_file(odd_path, index_bytes, true);
    MappedFile even_file(even_path, index_bytes, true);
    build_manacher(text, odd_file, even_file, c.size);
    run_query_benchmark(text, odd_file, even_file, c, planted);

    const double total_elapsed = seconds_since(total_start);
    print_stage("Total wall-clock time", total_elapsed);
    write_report(c, total_elapsed, fs::path("results") / "benchmark.csv");

    std::cout << "\n[Done] All stages completed.\n";
    return 0;
  }
  catch (const std::exception& e)
  {
    std::cerr << "\n[FATAL] " << e.what() << "\n";
    return 1;
  }
}
