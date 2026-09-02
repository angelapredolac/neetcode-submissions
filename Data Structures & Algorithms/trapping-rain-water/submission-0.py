class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        l, r = 0, len(height)-1

        max_l = height[l]
        max_r = height[r]

        trapped_water = 0

        while l<r:
            if max_l <= max_r:
                l +=1
                max_l = max(max_l, height[l])

                trapped_water += max_l-height[l]
            
            else:
                r-=1
                max_r = max(max_r, height[r])

                trapped_water += max_r-height[r]
        
        return trapped_water
            



            


"""
when you find a max scan for next greater than or equal
0
2 --> max_l=2
0 --> less than left and right so add 2 (min of left and right)
3 -> max_l=3
1 -> less than left and right so add 3-1=2 
0 -> less than left and right so 
"""

