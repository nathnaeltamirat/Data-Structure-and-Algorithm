class Solution:
    def racecar(self, target: int) -> int:
        fuel = [0,1]

        #count pos speed
        q = deque([(0,0,1),])
        visited = set([(0,1)])

        def calc(choice,pos,speed):
            if choice == 0:
                if speed > 0:
                    speed = - 1
                    return (pos,speed)
                return (pos,1)
            else:
                pos += speed
                speed *= 2
                return (pos,speed)
        while q:
            count, pos, speed = q.popleft()
            # print(count,pos,speed)
            for i in fuel:
                new_pos, new_speed = calc(i,pos,speed)
                if new_pos == target:
                    return count + 1
                if (new_pos,new_speed) not in visited:
                    q.append((count +1,new_pos,new_speed))
                    visited.add((new_pos,new_speed))


        