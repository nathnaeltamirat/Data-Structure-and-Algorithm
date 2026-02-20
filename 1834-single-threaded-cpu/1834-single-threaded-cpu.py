class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([e_time, p_time, idx] for idx, (e_time,p_time) in enumerate(tasks))
        # print(sorted)
        processor = []
        end_index = 0
        curr_time = tasks[0][0]
        def cpuStarter(index):
            nonlocal end_index
            #sorting based on processing time then index
            heappush(processor,(tasks[index][1],tasks[index][2]))
            #starting the cpu
            for i in range(index+1,len(tasks)):
                time = tasks[i][0]
                if time != curr_time:
                    break
                heappush(processor,(tasks[i][1],tasks[i][2]))
                end_index = i
            
        cpuStarter(0)
        res = []


        #cpu processing
        while processor:
            # print(processor)
            processed_time,index = heappop(processor)
            res.append(index)
            curr_time += processed_time
            if not processor and end_index + 1 < len(tasks):
                if tasks[end_index + 1][0] > curr_time:
                    curr_time = tasks[end_index + 1][0]
                    end_index = end_index+1
                    cpuStarter(end_index)
                    continue
            for i in range(end_index+1,len(tasks)):
                time = tasks[i][0]
                if time > curr_time:
                    break
                heappush(processor,(tasks[i][1],tasks[i][2]))
                end_index = i
        return res


            
