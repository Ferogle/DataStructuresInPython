import sys
input = sys.stdin.readline
MOD = 1000000007
MOD2 = 998244353
ii = lambda: int(input())
si = lambda: input()
dgl = lambda: list(map(int, input()))
f = lambda: map(int, input().split())
il = lambda: list(map(int, input().split()))
ls = lambda: list(input())
let = 'abcdefghijklmnopqrstuvwxyz'

def queryTree(arr,ind,lt,rt,sgt,low,high):
    if low>rt or high<lt:
        return 0
    if low<=lt<=rt<=high:
        return sgt[ind]
    mid=(lt+rt)//2
    return queryTree(arr,2*ind,lt,mid,sgt,low,high)+queryTree(arr,(2*ind)+1,mid+1,rt,sgt,low,high)

def updateTree(arr,ind,lt,rt,sgt,idx,val):
    if rt==lt:
        arr[idx]=val
        sgt[ind]=val
        return
    md = (lt+rt)//2
    if idx>md:
        updateTree(arr,2*ind+1,md+1,rt,sgt,idx,val)
    else:
        updateTree(arr,2*ind,lt,md,sgt,idx,val)
    sgt[ind]=sgt[2*ind]+sgt[2*ind+1]

def buildTree(arr, ind, lt, rt, sgt):
    if lt == rt:
        sgt[ind] = arr[lt]
        return
    buildTree(arr, 2 * ind, lt, (lt + rt) // 2, sgt)
    buildTree(arr, (2 * ind) + 1, (lt + rt) // 2 + 1, rt, sgt)
    sgt[ind] = sgt[2 * ind] + sgt[2 * ind + 1]

n = ii()
l = il()
sgt = [0] * (n * 2)                       # optimal size for array is 4*n
buildTree(l, 1, 0, n - 1, sgt)
updateTree(l,1,0,n-1,sgt,1,10)
print(queryTree(l,1,0,n-1,sgt,1,3))
