class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = []
        a = list(a)
        b = list(b)
        a.reverse()
        b.reverse()
        max_len = max(len(a), len(b))
        for i in range(max_len):
            bit_a = int(a[i]) if i < len(a) else 0
            bit_b = int(b[i]) if i < len(b) else 0
            total = bit_a + bit_b + carry
            carry = total // 2
            result.append(total % 2)
        if carry:
            result.append(carry)
        return ''.join(map(str, result[::-1]))
if __name__ == "__main__":
    solution = Solution()
    print(solution.addBinary("11", "1"))  
