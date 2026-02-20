class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count = Counter(words)
        holder = []
        big_length = len(max(words))
        def reverse_lex_key(s):
            l_order = [-ord(c) for c in s]
            if len(l_order) < big_length:
                l_order.append(0)
            return l_order
        for key, value in count.items():
            reversed_key = reverse_lex_key(key)
            holder.append((value,reversed_key,key))
        heapify(holder)
        print(holder)
        while len(holder) > k:
            heappop(holder)
        heapify_max(holder)
        print(holder)
        res = []
        while holder:
            res.append(heappop_max(holder)[2])
        print(holder)
        return res