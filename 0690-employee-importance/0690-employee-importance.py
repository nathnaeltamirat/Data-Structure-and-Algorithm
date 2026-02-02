"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        #mapping employess id to ag graph

        graph = defaultdict(list)
        for employee in employees:
            graph[employee.id].append(employee.importance)
            graph[employee.id].append(employee.subordinates)
        res = 0
        def dfs(id):
            nonlocal res
            res += graph[id][0]

            for neigh in graph[id][1]:
                dfs(neigh)
        dfs(id)
        return res