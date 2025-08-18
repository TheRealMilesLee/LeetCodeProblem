#!/usr/bin/env python3
"""
LeetCode Problem Test Runner
运行所有章节的测试用例
"""
import os
import subprocess
import sys


def run_tests():
  """运行所有测试"""
  print("🚀 开始运行 LeetCode 问题测试...")
  print("=" * 60)

  # 确保我们在正确的目录中
  script_dir = os.path.dirname(os.path.abspath(__file__))
  os.chdir(script_dir)

  # 测试文件列表
  test_files = [
      "Tests/test_chapter1_array_hashing.py",
      "Tests/test_chapter2_two_pointer.py", "Tests/test_chapter3_stack.py",
      "Tests/test_chapter4_binary_search.py",
      "Tests/test_chapter5_sliding_window.py",
      "Tests/test_dynamic_programming.py"
  ]

  total_passed = 0
  total_failed = 0

  for test_file in test_files:
    if os.path.exists(test_file):
      print(f"\n📝 运行测试: {test_file}")
      print("-" * 40)

      try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", test_file, "-v"],
            capture_output=True,
            text=True,
            timeout=60)

        if result.returncode == 0:
          print(f"✅ {test_file} - 所有测试通过!")
          # 计算通过的测试数量
          passed_count = result.stdout.count("PASSED")
          total_passed += passed_count
        else:
          print(f"❌ {test_file} - 有测试失败")
          print("错误输出:")
          print(result.stdout)
          print(result.stderr)
          failed_count = result.stdout.count("FAILED")
          total_failed += failed_count

      except subprocess.TimeoutExpired:
        print(f"⏰ {test_file} - 测试超时")
        total_failed += 1
      except Exception as e:
        print(f"💥 {test_file} - 运行时发生错误: {e}")
        total_failed += 1
    else:
      print(f"⚠️  测试文件不存在: {test_file}")

  # 最终结果
  print("\n" + "=" * 60)
  print("📊 测试总结:")
  print(f"✅ 通过的测试: {total_passed}")
  print(f"❌ 失败的测试: {total_failed}")
  print(f"📈 成功率: {total_passed / (total_passed + total_failed) * 100:.1f}%" if
        (total_passed + total_failed) > 0 else "📈 成功率: N/A")

  if total_failed == 0:
    print("🎉 所有测试都通过了!")
    return 0
  else:
    print("🔧 有些测试失败了，请检查代码实现")
    return 1


def run_specific_chapter(chapter):
  """运行特定章节的测试"""
  chapter_files = {
      "1": "Tests/test_chapter1_array_hashing.py",
      "2": "Tests/test_chapter2_two_pointer.py",
      "3": "Tests/test_chapter3_stack.py",
      "4": "Tests/test_chapter4_binary_search.py",
      "5": "Tests/test_chapter5_sliding_window.py",
      "dp": "Tests/test_dynamic_programming.py"
  }

  if chapter in chapter_files:
    test_file = chapter_files[chapter]
    if os.path.exists(test_file):
      print(f"🚀 运行 Chapter {chapter} 测试...")
      subprocess.run([sys.executable, "-m", "pytest", test_file, "-v"])
    else:
      print(f"❌ 测试文件不存在: {test_file}")
  else:
    print(f"❌ 未知的章节: {chapter}")
    print("可用的章节: 1, 2, 3, 4, 5, dp")


if __name__ == "__main__":
  if len(sys.argv) > 1:
    # 运行特定章节的测试
    chapter = sys.argv[1].lower()
    run_specific_chapter(chapter)
  else:
    # 运行所有测试
    exit_code = run_tests()
    sys.exit(exit_code)
