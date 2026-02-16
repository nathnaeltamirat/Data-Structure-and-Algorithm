class Solution:
    def splitString(self, s: str) -> bool:
        def validator(arr,start):
            if len(arr) == 1 and start == len(s):
                return False
            for i in range(1,len(arr)):
                if arr[i] - arr[i-1] != -1:
                    return False
            return True
        res = False
        def backtrack(start,arr):
            nonlocal res
            print(arr)
            if not validator(arr,start):
                return False
            if validator(arr,start) and start == len(s):
                print("True value ",arr)
                return True
            
            for i in range(start,len(s)):
                arr.append(int(s[start:i+1]))
                res = res or backtrack(i+1,arr)
                arr.pop()
            return res
            #0 
        return backtrack(0,[])
        return res
