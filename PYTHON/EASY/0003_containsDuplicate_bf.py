from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_nums = sorted(nums)
        for i in range(len(nums) - 1):
            if (new_nums[i] == new_nums[i+1]):
                return True
        return False
                
