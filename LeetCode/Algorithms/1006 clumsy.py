# 【中等】1006. 笨阶乘
# 通常，正整数 n 的阶乘是所有小于或等于 n 的正整数的乘积。例如，factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1。
# 相反，我们设计了一个笨阶乘 clumsy：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。
# 例如，clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1。
# 然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。
# 另外，我们使用的除法是地板除法（floor division），所以 10 * 9 / 8 等于 11。这保证结果是一个整数。
# 实现上面定义的笨函数：给定一个整数 N，它返回 N 的笨阶乘。


# class Solution:
#     def clumsy(self, N: int) -> int:
#         def f(N: int):
#             if N == 0: return 0
#             if N == 1: return 1
#             if N == 2: return 2
#             if N == 3: return 6
#             if N == 4: return 7
#             if N == 5: return 7
#             if N == 6: return 8
#             if N == 7: return 6
#             return N * (N-1) // (N-2) + (N-3) + f(N-4) - 2 * ((N-4) * (N-5) // (N-6))
#         return f(N)


# 找规律
class Solution:
    def clumsy(self, N: int) -> int:
        def f(N: int):
            if N == 0: return 0
            if N == 1: return 1
            if N == 2: return 2
            if N == 3: return 6
            if N == 4: return 7
            if N % 4 == 0: return N + 1
            if N % 4 == 1: return N + 2
            if N % 4 == 2: return N + 2
            if N % 4 == 3: return N - 1
        return f(N)


if __name__ == '__main__':
    s = Solution()

    result = 7
    N = 4
    print(s.clumsy(N))

    result = 12
    N = 10
    print(s.clumsy(N))