CXX := clang++
TARGET := build/palindrome_benchmark
SRC := src/PalindromeHighPerformance.cpp

CXXFLAGS := -std=c++20 -O3 -DNDEBUG -Wall -Wextra -Wpedantic -pthread
LDFLAGS := -pthread

.PHONY: all clean run-small run-100m run-1b help

all: $(TARGET)

$(TARGET): $(SRC)
	@mkdir -p build
	$(CXX) $(CXXFLAGS) $(SRC) $(LDFLAGS) -o $(TARGET)

run-small: all
	./$(TARGET) --size 1000000 --queries 100000 --threads 4

run-100m: all
	./$(TARGET) --size 100000000 --queries 1000000 --threads 4

run-1b: all
	./$(TARGET) --size 1000000000 --queries 10000000 --threads 4

clean:
	rm -rf build

help:
	@echo "make                 Build"
	@echo "make run-small       1M chars / 100K queries"
	@echo "make run-100m        100M chars / 1M queries"
	@echo "make run-1b          1B chars / 10M queries"
	@echo "make clean           Remove build output"
