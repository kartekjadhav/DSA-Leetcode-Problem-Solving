#TC - O(4*ALPHA) = O(1)
#SC - O(N+1)

class DisjointSet:
    def __init__(self,n) -> None:
        self.rank = [0]*(n+1)
        self.parent = [i for i in range(n+1)]
        self.size = [1 for _ in range(n+1)]
    
    def findPar(self,node) -> None:
        if node==self.parent[node]:
            return node
        self.parent[node] = self.findPar(self.parent[node])
        return self.parent[node]
    
    def unionRank(self,u,v):
        #pu and pv are ultimate parent of u and v respectively
        pu,pv = self.findPar(u), self.findPar(v)
        if pu==pv: return
        rankpu, rankpv = self.rank[pu], self.rank[pv]
        if rankpu < rankpv:
            self.parent[pu] = pv
        elif rankpv < rankpu:
            self.parent[pv] = pu
        else:
            self.parent[pv] = pu
            self.rank[u] += self.rank[v]
    
    def unionSize(self,u,v):
        #pu and pv are ultimate parent of u and v respectively
        pu,pv = self.findPar(u), self.findPar(v)
        if pu==pv: return
        sizeu, sizev = self.size[pu], self.size[pv]
        if sizeu < sizev:
            self.parent[pu] = pv
            self.size[pv] += self.size[pu]
        else:
            self.parent[pv] = pu
            self.size[pu] += self.size[pv]

#Optional Input
#v = int(input('Enter no. of vertex'))
#w = int(input('Enter no. of edges'))

#Creating Object
dsj = DisjointSet(7)
dsj.unionSize(1, 2)
dsj.unionSize(2, 3)
dsj.unionSize(4, 5)
dsj.unionSize(6, 7)
dsj.unionSize(5, 6)

#if 3 and 7 are in same component
if dsj.findPar(3)==dsj.findPar(7): print(True)
else: print(False)

dsj.unionSize(3, 7)

#if 3 and 7 are in same component
if dsj.findPar(3)==dsj.findPar(7): print(True)
else: print(False)