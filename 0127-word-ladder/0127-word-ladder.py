class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set([beginWord])
        q = deque([beginWord])
        def checker(a,b):
            count = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    count += 1
                if count > 1:
                    return False
            return True
        dist = 1
        while q:
            n = len(q)
            for _ in range(n):
                word = q.popleft()
                for word2 in wordList:
                    if word2 not in visited and checker(word,word2):
                        if word2 == endWord:
                            return dist + 1
                        q.append(word2)
                        visited.add(word2)
            dist += 1 




        return 0