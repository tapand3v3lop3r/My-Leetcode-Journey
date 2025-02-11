from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


# drastically reduced the time taken ...
# average time now = 3 ms
