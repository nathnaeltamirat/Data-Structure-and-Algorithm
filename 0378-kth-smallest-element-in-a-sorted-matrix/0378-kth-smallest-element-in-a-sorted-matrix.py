class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        min_heap = []
        #intialing the smallest value
        for i in range(n):
            val = matrix[i][0]
            heappush(min_heap,(val,i,0))
        i = 1
        while i < k:
            # print(min_heap)
            val,row, col = heappop(min_heap)
            if col < n-1:
                heappush(min_heap,(matrix[row][col+1],row,col+1))
            i+=1
        return min_heap[0][0]
        