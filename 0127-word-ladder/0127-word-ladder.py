class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        visited = set([beginWord])
        wordList = set(wordList)
        q = deque([beginWord])
        dist = 1
        while q:
            n = len(q)
            for _ in range(n):
                word = q.popleft()
                for i in range(len(word)):
                    for c in  'abcdefghijklmnopqrstuvwxyz':
                        if word[i] == c:
                            continue
                        new_word = word[:i] + c + word[i+1:]
                        if new_word not in visited and new_word in wordList:
                            if new_word == endWord:
                                return dist + 1
                            q.append(new_word)
                            visited.add(new_word)
            dist += 1 




        return 0