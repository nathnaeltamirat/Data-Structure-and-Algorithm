class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        res = [False]
        def backtrack(path,curr):
            if len(path) >= 3 and path[-1] != path[-2] + path[-3]:
                return False
            if len(num) == curr:
                return len(path) >= 3
            
            for i in range(curr,len(num)):
                if num[curr] == "0" and i > curr:
                    break
                path.append(int(num[curr:i+1]))
                res[0] = res[0] or backtrack(path,i+1)
                if res[0]:
                    return True
                path.pop()
            return res[0]
        return backtrack([],0)            