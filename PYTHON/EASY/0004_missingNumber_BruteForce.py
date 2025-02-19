# 268.  MISSING NUMBER

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new_nums = []
        for i in range(0, len(nums)+1):
            new_nums.append(i)

        missing_elements = list(set(new_nums) - set(nums))

        if missing_elements:
            return missing_elements[0]
        else:
            return None
