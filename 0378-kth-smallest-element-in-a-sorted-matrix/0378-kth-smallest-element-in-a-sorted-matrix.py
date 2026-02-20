class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def countLessThanK(middle):
            row =  n - 1
            col = 0
            count = 0
            while row >= 0 and col < n:
                if matrix[row][col] <= middle:
                    count += row + 1
                    col += 1
                else:
                    row -= 1
            return count 
        low = matrix[0][0]
        high = matrix[n-1][n-1]
        while low < high:
            middle  = low + (high - low)//2
            if countLessThanK(middle) < k:
                low = middle + 1
            else:
                high = middle
        return low