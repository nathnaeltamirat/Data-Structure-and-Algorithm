class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)

        def checker(max_count):
            curr_d = 1
            curr_s = 0
            i = 0
            while i < len(weights):
                if curr_s + weights[i] > max_count:
                    curr_d += 1
                    curr_s = weights[i]
                else:
                    curr_s += weights[i]
                i += 1
            return curr_d <= days
        while low <= high:
            middle = low + (high - low )//2
            if checker(middle):
                high = middle - 1
            else:
                low = middle + 1
        return low
                
            