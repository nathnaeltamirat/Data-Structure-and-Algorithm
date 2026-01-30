class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        half = total // 2

        a, b = (nums1),(nums2)
        if len(a) > len(b):
             a, b = b , a 
        
        low = 0
        high = len(a) - 1
        while True:
            i = low + (high - low)//2
            j = half - i - 2
            aleft = a[i] if i >= 0  else float('-inf')
            aright = a[i + 1 ] if (i+1) < len(a) else float('inf')
            bleft = b[j] if j >= 0 else float('-inf')
            bright = b[j+1] if (j+1) < len(b) else float('inf')
            if aleft <= bright and bleft <= aright:
                if total % 2:
                    return min(aright,bright)
                return (max(aleft,bleft) + min(aright,bright))/2
            elif aright < bleft:
                low+=1
            else:
                high -= 1
