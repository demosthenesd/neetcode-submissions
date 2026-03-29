from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        top, bot = 0, len(matrix) - 1
        theRow = None

        # 1) Binary search to find the candidate row
        while top <= bot:
            mid = (top + bot) // 2
            row = matrix[mid]

            if target < row[0]:
                bot = mid - 1
            elif target > row[-1]:
                top = mid + 1
            else:
                theRow = row
                break

        if theRow is None:
            return False

        # 2) Binary search inside that row
        l, r = 0, len(theRow) - 1
        while l <= r:
            mid = (l + r) // 2
            if theRow[mid] == target:
                return True
            elif theRow[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return False
