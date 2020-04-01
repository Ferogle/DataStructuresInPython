import sys
input = sys.stdin.readline
MOD = 1000000007
MOD2 = 998244353
ii = lambda: int(input().strip('\n'))
si = lambda: input()
dgl = lambda: list(map(int, input().strip('\n')))
f = lambda: map(int, input().strip('\n').split())
il = lambda: list(map(int, input().strip('\n').split()))
ls = lambda: list(input().strip('\n'))
let = 'abcdefghijklmnopqrstuvwxyz'

def updateBIT(i,bit,val,n):
    while i<=n:
        bit[i]+=val
        i+=i&(-i)

def queryBIT(i,bit):
    ans=0
    while i>0:
        ans+=bit[i]
        i-=i&(-i)
    return ans

n=ii()
l=il()
bit=[0 for i in range(n+10)]
for i in range(1,n+1):
    updateBIT(i,bit,l[i-1],n)
for _ in range(ii()):
    a,b=f()
    print(queryBIT(b,bit)-queryBIT(a-1,bit))
