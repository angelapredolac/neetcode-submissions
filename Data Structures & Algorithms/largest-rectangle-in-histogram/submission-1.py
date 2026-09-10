class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = [] # (start_index, height)

        for i, height in enumerate(heights):
            start = i

            # current bar ends all taller rectangles 
            while stack and stack[-1][1]>=height:
                index, prev_height = stack.pop()
                width = i-index
                max_area = max(max_area, prev_height*width)

                # current shorter bar can extend back to this index
                start = index
            
            stack.append((start, height))

        # remaining rectangles extend through the end
        n = len(heights)

        for index, height in stack:
            max_area = max(max_area, height*(n-index))
        
        return max_area


"""
pos 0: 7
pos 1: 
pos 3: 7 (max: 7, running max: 3)
pos 4:4 (max: 7, running max: 4)
pos 5: 5 (max: 7, running max: 5)

"""