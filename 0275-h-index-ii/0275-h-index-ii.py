class Solution:
    def hIndex(self, citations: List[int]) -> int:
        low = 0
        high = len(citations) - 1
        while low <= high:
            middle = low + (high - low)//2
            if citations[middle] >=  len(citations) - middle:
                high = middle - 1
            else:
                low = middle + 1
        return len(citations) - low