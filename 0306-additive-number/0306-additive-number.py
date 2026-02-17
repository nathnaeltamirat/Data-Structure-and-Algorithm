class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False

        def checker(arr):
            for i in range(2,len(arr)):
                if arr[i-1] + arr[i-2] != arr[i]:
                    return False
            return True
        self.res = False
        def backtrack(curr,path):

            if len(path) >= 3 and  path[-1] != path[-2] + path[-3]:
                return False
            if curr == len(num):
                return len(path) >= 3
            for i in range(curr,len(num)):
                if num[curr] == "0" and i > curr:
                    break
                path.append(int(num[curr:i+1]))
                self.res = self.res or backtrack(i+1,path)
                print(path)
                if self.res:
                    return True
                path.pop()
            return False
        backtrack(0,[])
        return self.res
