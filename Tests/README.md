# LeetCode Problems Tests

本目录包含了对所有 LeetCode 问题的 pytest 测试用例。

## 测试结构

```
Tests/
├── test_chapter1_array_hashing.py      # Chapter 1: 数组和哈希表
├── test_chapter2_two_pointer.py        # Chapter 2: 双指针
├── test_chapter3_stack.py              # Chapter 3: 栈
├── test_chapter4_binary_search.py      # Chapter 4: 二分搜索
├── test_chapter5_sliding_window.py     # Chapter 5: 滑动窗口
└── test_dynamic_programming.py         # 动态规划
```

## 如何运行测试

### 1. 安装依赖
```bash
pip install pytest
```

### 2. 运行所有测试
```bash
# 方法 1: 使用 pytest 直接运行
pytest Tests/ -v

# 方法 2: 使用提供的脚本
python run_tests.py
```

### 3. 运行特定章节的测试
```bash
# 运行 Chapter 1 测试
python run_tests.py 1

# 运行 Chapter 2 测试
python run_tests.py 2

# 运行动态规划测试
python run_tests.py dp

# 或者直接使用 pytest
pytest Tests/test_chapter1_array_hashing.py -v
```

### 4. 运行特定测试类或测试方法
```bash
# 运行特定测试类
pytest Tests/test_chapter1_array_hashing.py::TestContainsDuplicate -v

# 运行特定测试方法
pytest Tests/test_chapter1_array_hashing.py::TestContainsDuplicate::test_contains_duplicate_true -v
```

## 测试覆盖的内容

每个测试文件包含以下类型的测试用例：

- ✅ **基本功能测试**: 验证算法的基本功能
- ✅ **边界条件测试**: 测试空输入、单元素等边界情况
- ✅ **错误情况测试**: 测试无解或异常输入的处理
- ✅ **性能测试**: 验证算法在合理时间内完成

## 注意事项

1. **导入问题**: 如果遇到导入错误，请确保所有的 Solution 类都正确实现
2. **方法名称**: 测试假设每个文件中的类名为 `Solution`，如果不同请修改测试文件
3. **返回值**: 请确保你的实现返回的数据类型与测试期望的一致
4. **超时**: 某些测试可能会超时，这通常表示算法效率需要优化

## 示例输出

```
Tests/test_chapter1_array_hashing.py::TestContainsDuplicate::test_contains_duplicate_true PASSED
Tests/test_chapter1_array_hashing.py::TestContainsDuplicate::test_contains_duplicate_false PASSED
Tests/test_chapter1_array_hashing.py::TestValidAnagram::test_valid_anagram PASSED
...
================================ 45 passed in 2.34s ================================
```

## 故障排除

如果测试失败，请检查：

1. 你的 Solution 类是否正确实现了所需的方法
2. 方法的参数和返回值类型是否正确
3. 算法逻辑是否处理了所有边界条件
4. 是否有语法错误或运行时错误

## 贡献

如果你发现测试用例有问题或想要添加更多测试，请：

1. Fork 这个仓库
2. 创建新的测试用例
3. 确保所有测试通过
4. 提交 Pull Request
