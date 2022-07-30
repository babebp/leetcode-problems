class Solution:
    def firstMissingPositive(self, nums):
        nums.sort()
        number = 1
        
        for i in nums:
            if number == i:
                number += 1
                
        return number