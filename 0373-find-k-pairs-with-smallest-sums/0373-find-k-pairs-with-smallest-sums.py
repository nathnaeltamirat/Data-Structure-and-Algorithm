class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = [(nums1[0] + nums2[0],0,0)]
        i = 0 
        res = []
        while i < k:
            _,r, c = heappop(min_heap)
            res.append([nums1[r],nums2[c]])
            if c + 1 < len(nums2):

                summation = nums1[r] + nums2[c+1]
                heappush(min_heap,(summation,r,c+1))
            
            if c == 0 and r + 1 < len(nums1):
                summation = nums1[r+1] + nums2[c]
                heappush(min_heap,(summation,r+1,c))
            i+=1
        return res
        
                
