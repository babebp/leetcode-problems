class Solution:
    def climbStairs(self, n: int) -> int:
        num_1 , num_0 = 1, 0
        
        for i in range(n):
            num_1 , num_0 = num_1 + num_0, num_1
            
        return num_1

# LINK : https://leetcode.com/problems/climbing-stairs/