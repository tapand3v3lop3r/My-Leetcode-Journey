from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = []
        
        for num in nums:
            if num not in temp:
                temp.append(num)

      
        for i in range(len(temp)):
            nums[i] = temp[i]
        
        return len(temp)
