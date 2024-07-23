class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        one_step_back = 1
        two_steps_back = 1
        for i in range(2, n + 1):
            current = one_step_back + two_steps_back
            two_steps_back = one_step_back
            one_step_back = current
        return one_step_back
solution = Solution()
print(solution.climbStairs(2))  
