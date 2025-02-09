from typing import List

# Time Limit Exceeded - Case 50/65 and 51/65
class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count, len_nums = 0, len(nums)
        for i in range(len_nums-1):
            for j in range(i+1, len_nums):
                if (j-i != nums[j] - nums[i]):
                    count += 1
        return count