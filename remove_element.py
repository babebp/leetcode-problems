class Solution:
    def removeElement(self, nums, val):
        count = 0
        while val in nums:
            count += 1
            nums.remove(val)