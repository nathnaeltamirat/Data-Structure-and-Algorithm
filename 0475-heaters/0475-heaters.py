class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def checker(r):
            i = 0
            j = 0
            while i < len(houses):
                while j < len(heaters) and heaters[j] + r < houses[i]:
                    j += 1
                if j == len(heaters) or heaters[j] - r >houses[i]:
                    return False
                i+=1
            return True
        low = 0
        high = 10 ** 9
        while low <= high:
            middle = low + (high - low)//2
            if checker(middle):
                high = middle - 1
            else:
                low = middle + 1
        return low