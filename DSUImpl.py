#solution to the question 277A on cfrcs using DSU

MOD = 1000000007
MOD2 = 998244353
ii = lambda : int(input())
si = lambda : input()
dgl = lambda : list(map(int, input()))
f = lambda : map(int, input().split())
il = lambda : list(map(int, input().split()))
ls = lambda : list(input())

class DSU:                                                  #DSU class
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[1 for i in range(n)]
    def find_set(self,a):
        if a==self.parent[a]:
            return a
        self.parent[a]=self.find_set(self.parent[a])
        return self.parent[a]
    def union_set(self,a,b):
        x=self.find_set(a)
        y=self.find_set(b)
        if x!=y:
            if self.rank[x]<self.rank[y]:
                x,y=y,x
            self.rank[x]+=self.rank[y]
            self.parent[y]=x

n,m=f()
l=[];c=0
for _ in range(n):
    a,*b=f();b=set(b)
    if len(b):l.append(b)
    else:c+=1
nn=len(l)
dsu=DSU(nn)
par=-1
for i in range(1,m+1):
    for j in range(nn):
        if i in l[j]:
            if par==-1:par=j
            else:dsu.union_set(par,j)
    par=-1
print(max(len(set(dsu.find_set(i) for i in range(nn)))-1,0)+c)
