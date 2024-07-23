class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        factorials = [1] * n
        for i in range(1, n):
            factorials[i] = factorials[i - 1] * i
        k -= 1
        result = []
        for i in range(n, 0, -1):
            idx = k // factorials[i - 1]
            result.append(str(numbers[idx]))
            numbers.pop(idx)
            k %= factorials[i - 1]
        return ''.join(result)
solution = Solution()
print(solution.getPermutation(3, 3)) 
print(solution.getPermutation(4, 9))  
print(solution.getPermutation(3, 1))  
