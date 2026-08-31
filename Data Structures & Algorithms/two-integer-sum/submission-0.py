class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_ind = {}
        for i, num in enumerate(nums):
            if target-num in val_to_ind.keys():
                return [val_to_ind[target-num], i]
            val_to_ind[num] = i
        