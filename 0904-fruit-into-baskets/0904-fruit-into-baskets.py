class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        l = 0
        res = 0
        for r in range(len(fruits)):
            while fruits[r] not in basket and len(basket) == 2:
                basket[fruits[l]] -= 1
                if basket[fruits[l]] == 0:
                    basket.pop(fruits[l])
                l += 1
            print(l,r)
            basket[fruits[r]] += 1
            res = max(res, r-l +1)
        return res