class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total_sum = 0
        row, column = len(grid), len(grid[0])
        for i in range(row):
            for j in range(column):
                total_sum += grid[i][j]

        #checking horizontal cut approach
        left = total_sum
        curr = 0
        for i in range(row):
            for j in range(column):
                curr += grid[i][j]
                left -= grid[i][j]
                if curr == left and j == column -1:
                    print("first")
                    return True
        
        #checking vertical cut approach
        left = total_sum
        curr = 0
        i = j = 0
        while True:
            if i == row  or j == column:
                break
            if  i < row - 1:
                left -= grid[i][j]
                curr += grid[i][j]
                i+=1
            elif i == row - 1:
                left -= grid[i][j]
                curr += grid[i][j]
                if left == curr:
                    return True
                if j < column -1:
                    i = 0
                j += 1

        return False 
