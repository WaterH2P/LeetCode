# 1323. 6 和 9 组成的最大数字
# 给你一个仅由数字 6 和 9 组成的正整数 num。
# 你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。
# 请返回你可以得到的最大数字。

class Solution:
  def maximum69Number (self, num: int) -> int:
    return int(str(num).replace('6', '9', 1))

if __name__ == '__main__':
  s = Solution()
  print(s.maximum69Number(9969))