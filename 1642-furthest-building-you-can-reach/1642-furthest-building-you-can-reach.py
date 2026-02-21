class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        order_heap = []
        for i in range(1,len(heights)):
            if heights[i] > heights[i-1]:
                diff = heights[i] - heights[i-1]
                heappush(order_heap,(diff,i))
                if len(order_heap) > ladders:
                    if bricks >= order_heap[0][0]:
                        bricks-= order_heap[0][0]
                        heappop(order_heap)
                    else:
                        return i -1
                    
        return len(heights)-1

                
