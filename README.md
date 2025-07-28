# LeetCodeProblem
## Project Overview
This repository contains solutions to various LeetCode problems implemented in Python. The project is organized by topics with Chapter1 focusing on Array and Hashing problems, along with Dynamic Programming solutions.

## Directory Structure
```
.
├── Chapter1-ArrayHashing/
│   ├── 1-ContainsDuplicate.py
│   ├── 2-ValidAnagram.py
│   ├── 3-TwoSum.py
│   ├── 4-GroupAnagrams.py
│   ├── 5-TopKFrequent.py
│   ├── 6-EncodeDecodeString.py
│   ├── 7-ProductOfArray.py
│   ├── 8-ValidSudoku.py
│   └── 9-LongestCommonSequence.py
├── DynamicProgramming/
│   ├── DP-CoinChange.py
│   └── DP-RodCutting.py
├── LICENSE
└── README.md
```

## Chapter 1: Array & Hashing Problems
- `1-ContainsDuplicate.py`: Check if array contains duplicate elements
- `2-ValidAnagram.py`: Validate if two strings are anagrams
- `3-TwoSum.py`: Find two numbers that add up to target sum
- `4-GroupAnagrams.py`: Group strings that are anagrams together
- `5-TopKFrequent.py`: Find k most frequent elements in array
- `6-EncodeDecodeString.py`: Encode/decode list of strings to single string
- `7-ProductOfArray.py`: Product of array except self
- `8-ValidSudoku.py`: Validate Sudoku board rules
- `9-LongestCommonSequence.py`: Find longest consecutive sequence

## Dynamic Programming
- `DP-CoinChange.py`: Coin change problem solution
- `DP-RodCutting.py`: Rod cutting optimization problem

## Language
Python

---

# LeetCodeProblem
## 项目简介
本项目包含多个LeetCode算法题解，采用Python实现。项目按主题分类，第一章专注于数组和哈希表问题，另外包含动态规划相关解题方案。

## 目录结构
```
.
├── Chapter1-ArrayHashing/
│   ├── 1-ContainsDuplicate.py        # 检查数组是否包含重复元素
│   ├── 2-ValidAnagram.py             # 验证字母异位词
│   ├── 3-TwoSum.py                   # 两数之和
│   ├── 4-GroupAnagrams.py            # 分组异位词
│   ├── 5-TopKFrequent.py             # 前K个高频元素
│   ├── 6-EncodeDecodeString.py       # 字符串编码解码
│   ├── 7-ProductOfArray.py           # 除自身以外数组的乘积
│   ├── 8-ValidSudoku.py              # 有效的数独
│   └── 9-LongestCommonSequence.py    # 最长连续序列
├── DynamicProgramming/
│   ├── DP-CoinChange.py              # 硬币找零问题
│   └── DP-RodCutting.py              # 钢条切割问题
├── LICENSE
└── README.md
```

## 第一章：数组与哈希表
本章包含9个经典的数组和哈希表问题：

1. **包含重复元素** - 使用哈希表检测数组中的重复值
2. **有效的字母异位词** - 字符频次统计验证异位词
3. **两数之和** - 哈希表优化的目标和查找
4. **字母异位词分组** - 基于字符频次的分组策略
5. **前K个高频元素** - 桶排序实现的频次统计
6. **字符串编码解码** - 长度标记的编码解码方案
7. **除自身以外数组的乘积** - 前缀后缀乘积的优化算法
8. **有效的数独** - 行列九宫格的哈希集合验证
9. **最长连续序列** - O(n)时间复杂度的序列查找

## 动态规划专题
- **硬币找零问题** - 经典的动态规划入门问题
- **钢条切割问题** - 最优子结构的动态规划应用

## 技术说明
- 主要开发语言: Python
- 代码规范: PEP8格式标准
- 算法复杂度: 每个解法都注重时间和空间复杂度优化
- 数据结构: 重点使用数组、哈希表、集合等基础数据结构
## 使用说明
1. 克隆项目仓库
2. 安装Python环境
3. 直接运行`.py`文件或通过IDE打开`.vscode`配置文件
4. 通过单元测试验证算法正确性
## 贡献指南
欢迎提交以下类型的贡献：
- 新增LeetCode题解
- 优化现有算法实现
- 修复代码错误
- 完善文档说明
## 许可证
项目采用MIT许可证，详见LICENSE文件
## 注意事项
1. 项目包含Git版本控制相关文件
2. 示例代码已通过基础测试
3. 请确保使用Python 3.x环境
4. 避免直接提交编译生成文件到主分支
