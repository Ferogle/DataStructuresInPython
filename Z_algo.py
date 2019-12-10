MOD = 1000000007
ii = lambda : int(input())
si = lambda : input()
dgl = lambda : list(map(int, input()))
f = lambda : map(int, input().split())
il = lambda : list(map(int, input().split()))
ls = lambda : list(input())
#Z-algortihm for pattern matching
def ZLPS(x,lps):
    lx=len(x)
    lt,rt=0,0
    for i in range(1,lx):
        if i>rt:        #when i is not in between l and r
            lt,rt=i,i
            while rt<lx and x[rt]==x[rt-lt]:    #increase r till maximum matching substring is obtained
                rt+=1
            lps[i]=rt-lt
            rt-=1
        else:
            if lps[i-lt]<=rt-i:  #when the previous LPS value is within L and R
                lps[i]=lps[i-lt]
            else:
                lt=i
                while rt<lx and x[rt]==x[rt-lt]:   #if previous values exceeds L and R then increment R
                    rt+=1
                lps[i]=rt-lt
                rt-=1
def ZSearch(stg,pat):
    x=pat+'$'+stg
    lp=len(pat)
    ln=len(stg)
    lps=[0]*len(x)
    ZLPS(x,lps)
    print(*lps)
    for i in range(len(x)):
        if lps[i]==lp:
            print(i-lp-1,end=' ')
stg="aabyaabybaabyaabyaax"
pat="aabyaaby"
ZSearch(stg,pat)
