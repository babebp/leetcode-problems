class Solution:
    def mySqrt(self, x: int) -> int:
        begin = 0
        end = x
        
        while begin <= x:
            mid = begin + (end - begin) // 2
            
            if mid * mid <= x < (mid+1)*(mid+1):
                return mid
            elif x < mid * mid:
                end = mid - 1
            else:
                begin = mid + 1