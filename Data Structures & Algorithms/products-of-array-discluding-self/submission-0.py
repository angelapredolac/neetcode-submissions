class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix_prods = [1 for _ in range(n)]
        suffix_prods = [1 for _ in range(n)]
        output = []

        # prefix_prods is everything to the left of i
        for i in range(1, n):
            prefix_prods[i] = prefix_prods[i-1] * nums[i-1]
        
        # suffix_prods is everything to the right of i
        for i in range(n-2, -1, -1):
            suffix_prods[i] = suffix_prods[i+1] * nums[i+1]

        for i in range(n):
            output.append(prefix_prods[i]*suffix_prods[i])
        
        return output



        