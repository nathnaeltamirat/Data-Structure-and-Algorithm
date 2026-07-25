class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        #edge case
        if (endWord not in wordList) or (endWord == beginWord):
            return 0
        
        def checker(s1,s2):
            count = 0
            for i in range(len(s1)):
                if s1[i] != s2[i]:
                    count += 1
            return count <= 1
        
        q = deque([beginWord])
        visited = set([beginWord])
        res = 1
        while q:
            n = len(q)
            res += 1
            for _ in range(n):
                baseWord = q.popleft()
                for word in wordList:
                    if word not in visited and checker(baseWord,word):
                        visited.add(word)
                        q.append(word)
                        if word == endWord:
                            return res
        
        return 0