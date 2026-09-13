class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, down = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        row = 0
        while top <= down:
            mid = (top + down) // 2

            if target < matrix[mid][0]:
                down = mid - 1
            elif target >= matrix[mid][0]:
                if target <= matrix[mid][right]:
                    row = mid
                    break
                top = mid + 1
        
        while left <= right:
            mid = (left + right) // 2

            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            elif target == matrix[row][mid]:
                return True
        
        return False
                
