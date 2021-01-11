from typing import List
class Solution240:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) - 1
        for m in range(len(matrix)):
            res_row = self.search(matrix[m], target)
            if m <= n:
                col_line = [i[m] for i in matrix[m:]]
                res_col = self.search(col_line, target)
                if res_col == True:
                    return True
            if res_row == True:
                return True

        return False

    def search(self, line: List[int], target: int) -> bool:
        start = 0
        end = len(line) - 1
        while start <= end:
            mid = start + (end - start) // 2
            if line[mid] == target:
                return True
            elif line[mid] < target:
                start = mid + 1
            elif line[mid] > target:
                end = mid - 1
        return False

# 方法二
class Solution:
    def searchMatrix(self, matrix, target):
        # an empty matrix obviously does not contain `target` (make this check
        # because we want to cache `width` for efficiency's sake)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        # cache these, as they won't change.
        height = len(matrix)
        width = len(matrix[0])

        # start our "pointer" in the bottom-left
        row = height - 1
        col = 0

        while col < width and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:  # found it
                return True

        return False


