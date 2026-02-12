class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        h_word_list = set(wordList)
        if endWord not in wordList:
            return 0
        q = deque([beginWord])
        visited = set([beginWord])
        dist = 1
        while q:
            n = len(q)
            for _ in range(n):
                word = q.popleft()
                for i in range(len(word)):
                    val = word[i]
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        if c == val:
                            continue
                        
                        new_word = word[:i] + c + word[i+1:]
                        if new_word in h_word_list:
                            if new_word not in visited:
                                q.append((new_word))
                                visited.add((new_word))
                                if new_word == endWord:
                                    return dist + 1
            dist += 1
        return 0