class UnionFind:
    def __init__(self):
        self.parent = dict()
        self.size = defaultdict(lambda:1)
    def find(self,x):
        if x not in self.parent:
            self.parent[x] = x
            return x
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                self.parent[rooty] = rootx
                self.size[rootx] += self.size[rooty]

            else:
                self.parent[rootx] = rooty
                self.size[rooty] += self.size[rootx]

    def isConnected(self,x,y):
        return self.find(x) == self.find(y)
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = UnionFind()
        person = defaultdict(str)
        all_emails = set()
        for account in accounts:
            name = account[0]
            emails = account[1:]
            for i in range(len(emails)):
                dsu.union(emails[i],emails[0])
                all_emails.add(emails[i])
                person[emails[i]] = name
        all_email = list(all_emails)
        email_groupped =defaultdict(list)
        for email in all_email:
            email_groupped[dsu.find(email)].append(email)
        res = []
        for key in email_groupped:
            name = person[key]
            temp = [name] + sorted(email_groupped[key])
            res.extend([temp])
        return res