class Solution:
    def searchRange(self, nums, target):
        begin = 0
        end = len(nums) - 1
        
        if target not in nums:
            return [-1, -1]
        
        if target in nums and len(nums) == 1:
            return [0, 0]
        
        while begin <= end:
            mid = begin + (end - begin) // 2
            
            if nums[mid] == target and nums[mid + 1] == target:
                return [mid, mid + 1]
            
            
            if nums[mid - 1] == target and nums[mid] == target:
                return [mid - 1, mid]
           
            
            elif nums[mid] > target:
                end = mid - 1
                
            else:
                begin = mid + 1

# LINK : https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/