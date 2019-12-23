MOD = 1000000007
ii = lambda : int(input())
si = lambda : input()
dgl = lambda : list(map(int, input()))
f = lambda : map(int, input().split())
il = lambda : list(map(int, input().split()))
ls = lambda : list(input())
#inplace Heap sort
'''insert and removeMin functions of priority queue 
were used with a little modification'''
def inplcehpsrt(pq,sz):
    for i in range(1,sz):
        CI = i
        while CI > 0:
            PI = (CI - 1) // 2
            if pq[PI] > pq[CI]:
                pq[CI], pq[PI] = pq[PI], pq[CI]
            else:
                break
            CI = PI
    size=sz
    for i in range(sz):
        pq[size-1],pq[0]=pq[0],pq[size-1]
        size-=1
        pi=0
        lci,rci=2*pi+1,2*pi+2
        while lci<size:
            mi=pi
            if pq[mi]>pq[lci]:
                mi=lci
            if rci<size and pq[rci]<pq[mi]:
                mi=rci
            if mi==pi:
                break
            pq[mi],pq[pi]=pq[pi],pq[mi]
            pi=mi
            lci, rci = 2 * pi + 1, 2 * pi + 2
    print(*pq)

l=[1,2,3,4,5,6]
inplcehpsrt(l,6)
