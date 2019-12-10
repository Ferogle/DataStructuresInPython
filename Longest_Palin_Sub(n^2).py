MOD = 1000000007
ii = lambda : int(input())
si = lambda : input()
dgl = lambda : list(map(int, input()))
f = lambda : map(int, input().split())
il = lambda : list(map(int, input().split()))
ls = lambda : list(input())

def LstPalSub(stg):
    n=len(stg)
    mx=0
    for i in range(1,n):
        l,r=i-1,i
        while l>=0 and r<n and stg[l]==stg[r]:
            mx=max(r-l+1,mx)
            l-=1
            r+=1
        l,r=i-1,i+1
        while l>=0 and r<n and stg[l]==stg[r]:
            mx=max(mx,r-l+1)
            r+=1
            l-=1
    print(mx)

stg='abbabbabb'
LstPalSub(stg)
