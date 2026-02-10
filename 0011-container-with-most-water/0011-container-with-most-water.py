class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            value = min(height[l],height[r])  * (r - l)
            # print(l,r,height[l] , height[r],value)
            res = max(res,value)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res
            
