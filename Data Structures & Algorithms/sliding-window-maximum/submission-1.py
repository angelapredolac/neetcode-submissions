from collections import deque
from typing import List 

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        result = []
        candidates = deque() # stores indices

        for right in range(len(nums)):
            # 1. remove elements that have left the window
            if candidates and candidates[0] <= right-k:
                candidates.popleft()
            
            # 2. maintain decreasing order of values
            while candidates and nums[candidates[-1]] <= nums[right]:
                candidates.pop()
            
            # 3. add the current index
            candidates.append(right)

            # 4. record the maximum once the first window is complete 
            if right >= k-1:   
                result.append(nums[candidates[0]])
        
        return result



        