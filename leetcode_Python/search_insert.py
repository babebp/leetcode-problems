class Solution:
    def searchInsert(self, nums, target):
        begin = 0
        end = len(nums) - 1
        
        while begin <= end:
            mid = begin + (end - begin) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                end = mid - 1
                
            else:
                begin = mid + 1
                
        return begin

# Link : https://leetcode.com/problems/search-insert-position/