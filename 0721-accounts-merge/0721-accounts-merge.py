class UnionFind:
    def __init__(self):
        self.root = dict()
        self.size = defaultdict(lambda:1)
    def find(self,x):
        if x not in self.root:
            self.root[x] = x
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.size[rootx] > self.size[rooty]:
                self.root[rooty] = rootx
                self.size[rootx] += self.size[rooty]
            else:
                self.root[rootx] = rooty
                self.size[rooty] += self.size[rootx]
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = UnionFind()
        email_to_person = {}
        all_emails = set()
        for i in range(len(accounts)):
            name, emails = accounts[i][0], accounts[i][1:]
            for j in range(len(emails)):
                dsu.union(emails[j],emails[0])
                email_to_person[emails[j]]  = name
                all_emails.add(emails[j])
        ordered = defaultdict(list)
        for email in all_emails:
            parent = dsu.find(email)
            ordered[parent].append(email)
        res = []
        for item in ordered:
            name = email_to_person[item]
            emails = sorted(ordered[item])
            temp = [name, *emails]
            res.append(temp)
        return res

