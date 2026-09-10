class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        row = 0
        # find the right row
        while row < len(matrix)-1 and matrix[row][-1] < target:
            row += 1
        
        l = 0
        r = len(matrix[row])-1
        
        while l<=r:
            mid = (l+r)//2
            if matrix[row][mid]==target:
                return True
            elif matrix[row][mid]>target:
                r = mid-1
            else:
                l = mid+1
        
        return False

        

        