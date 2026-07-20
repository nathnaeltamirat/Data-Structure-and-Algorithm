class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n!=0:
            last = m + n -1
            p , q = m-1, n-1
            while  q>=0 and p>=0:
                if nums2[q] > nums1[p]:
                    nums1[last] = nums2[q]
                    q-=1 
                else:
                    nums1[last] = nums1[p]
                    p-=1
                last-=1
            while q>=0:
                nums1[last] = nums2[q]
                q-=1
                last-=1

                