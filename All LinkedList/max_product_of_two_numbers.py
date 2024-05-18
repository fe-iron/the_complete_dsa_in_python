from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return -1
        max1, max2 = -1, -1
        for i in nums:
            if i > max1:
                max2 = max1
                max1 = i
            elif i > max2:
                max2 = i
        return (max1-1) * (max2-1)
        
