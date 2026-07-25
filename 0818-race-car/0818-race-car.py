class Solution:
    def racecar(self, target: int) -> int:
        items = ['a','r']
        #storing speed and position
        q = deque([(1,0)])
        visited = set([1,0])
        res = 0
        
        def speedAndPos(speed,pos,item):
            if item == 'a':
                pos += speed
                speed *=2
            else:
                if speed > 0:
                    speed = -1
                else:
                    speed = 1
            return [speed,pos]


        while True:
            n = len(q)
            res += 1
            for _ in range(n):
                speed,pos = q.popleft()
                for item in items:
                    new_speed, new_pos = speedAndPos(speed,pos,item)
                    if (new_speed, new_pos) not in visited:
                        visited.add((new_speed,new_pos))
                        q.append((new_speed,new_pos))
                        if new_pos == target:
                            return res
   
