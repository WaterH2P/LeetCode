class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467%n == 0

s = Solution()
print(s.isPowerOfThree(9))