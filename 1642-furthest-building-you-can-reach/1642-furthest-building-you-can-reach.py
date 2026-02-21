class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        def checker(building):
            c_ladder = ladders
            c_bricks = bricks
            order = []
            for i in range(1,building+1):
                if heights[i] > heights[i-1]:
                    order.append((heights[i] - heights[i-1]))
            order.sort(reverse = True)
            for i in range(len(order)):
                if c_ladder:
                    order[i] = 0
                    c_ladder -= 1
                if not c_ladder and c_bricks:
                    if c_bricks < order[i]:
                        return False
                    c_bricks -= order[i]
                    order[i] = 0
                
            return max(order) == 0 if order else True



        low = 0
        high = len(heights) - 1
        while low <= high:
            middle = low + (high - low)//2
            print(middle)
            if checker(middle):
                low = middle + 1
            else:
                high = middle - 1
        return high