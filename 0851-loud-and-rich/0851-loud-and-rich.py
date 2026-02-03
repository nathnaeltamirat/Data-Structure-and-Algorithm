class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for a, b in richer:
            graph[a].append(b)
            indegree[b] += 1
        q = deque()
        ans = [i for i in range(len(quiet))]
        for i in range(len(quiet)):
            if indegree[i] == 0:
                q.append(i)
                ans[i] = i
        while q:
            node = q.popleft()
            for neigh in graph[node]:
                indegree[neigh] -= 1
                if quiet[ans[node]] < quiet[ans[neigh]]:
                    ans[neigh] = ans[node]
                if indegree[neigh] == 0:
                    q.append(neigh)
        print(ans)
        return ans
