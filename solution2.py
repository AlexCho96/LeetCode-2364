from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n, freq, good_pairs = len(nums), {}, 0
        diff, total_pairs = [nums[i] - i for i in range(len(nums))], (n*(n-1)/2)
        
        for d in diff:
            if d in freq:
                freq[d] += 1
            else:
                freq[d] = 1
        
        for count in freq.values():
            if count >= 2:
                good_pairs += count * (count - 1) / 2
            
        bad_pairs = total_pairs - good_pairs
        return int(bad_pairs)