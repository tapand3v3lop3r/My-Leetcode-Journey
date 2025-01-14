from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []


nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.twoSum(nums, target)) 

'''
Time Complexity = O(n^2)
Space Complexity = O(1)
'''
