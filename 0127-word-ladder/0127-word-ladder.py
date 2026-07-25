class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        #edge case
        if (endWord not in wordList) or (endWord == beginWord):
            return 0
        
        pattern = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                p = word[:i] + "*" + word[i+1:]
                pattern[p].append(word)
        
        q = deque([(beginWord,1)])
        visited = set([beginWord])
        
        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist
            
            for i in range(len(word)):
                p = word[:i] + "*" + word[i+1:]
                for patt in pattern[p]:
                    if patt not in visited:
                        visited.add(patt)
                        q.append((patt,dist+1))
                pattern[p] = []
        return 0