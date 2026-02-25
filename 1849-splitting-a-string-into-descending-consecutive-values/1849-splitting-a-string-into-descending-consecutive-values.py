class Solution:
    def splitString(self, s: str) -> bool:
        def validate(path):
            for i in range(1,len(path)):
                if path[i-1] - path[i] != 1:
                    return False
            return True
        
        def backtrack(path,curr):
            val = False
            if curr == len(s):
                if validate(path) and len(path) > 1:
                    return True
                return False
            
            for i in range(curr,len(s)):
                path.append(int(s[curr:i+1]))
                # print(path)
                val = backtrack(path,i+1)
                if val:
                    return True
                path.pop()
            return val
        return backtrack([],0)
        
