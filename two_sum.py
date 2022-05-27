class Solution:
    def twoSum(self, nums, target):
        hash_map = {}
        
        for i in range(len(nums)):
            tmp = target - nums[i]
            
            if tmp in hash_map:
                return [i, hash_map[tmp]]
            
            else:
                hash_map[nums[i]] = i

