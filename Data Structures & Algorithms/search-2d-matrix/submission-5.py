class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        cols = len(matrix[0])

        top = 0
        bott = row - 1

        while top <= bott:
            mid = (top + bott)//2

            if target < matrix[mid][0]:
                bott = mid -1
            elif target > matrix[mid][cols -1]:
                top = mid + 1
            else:
                break
        if not (top <= bott):
            return False

        row = (top + bott)//2
        l = 0
        r = cols - 1
        while l <= r:
            mid = (l + r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False