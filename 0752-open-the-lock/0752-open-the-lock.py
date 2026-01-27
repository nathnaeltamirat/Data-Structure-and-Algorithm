class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if ("0000") in deadends:
            return -1
        if '0000' == target:
            return 0
        deadends.add("0000")
        q = deque(["0000"])
        graph = {
            '0': ['1', '9'],
            '1': ['0', '2'],
            '2': ['1', '3'],
            '3': ['2', '4'],
            '4': ['3', '5'],
            '5': ['4', '6'],
            '6': ['5', '7'],
            '7': ['6', '8'],
            '8': ['7', '9'],
            '9': ['8', '0']
            }

        dist = 0
        while q:
            n = len(q)
            dist += 1
            for _ in range(n):
                code = q.popleft()
                for i in range(len(code)):
                    for pos in graph[code[i]]:
                        new_code = code[0:i] + pos + code[i+1:]
                        if new_code not in deadends:
                            q.append(new_code)
                            deadends.add(new_code)
                            if new_code == target:
                                return dist
        return -1




        