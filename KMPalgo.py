MOD = 1000000007
ii = lambda : int(input())
si = lambda : input()
dgl = lambda : list(map(int, input()))
f = lambda : map(int, input().split())
il = lambda : list(map(int, input().split()))
ls = lambda : list(input())

def LPS(stg):#example explained is 'adadabadadabadadad'
    ln=len(stg)
    lps=[0]*ln
    i,j=1,0
    while i<ln:
        if stg[i]==stg[j]:
            lps[i]=j+1
            i+=1
            j+=1
        else:
            if j==0:
                lps[i]=0
                i+=1
            else:
                j=lps[j-1]
    return lps

def KMPSearch(stg,pat):     #stg='abcxabcdabcdabcy'
                            #pat='abcdabcx'
    lns=len(stg)
    lnp=len(pat)
    i,j=0,0
    lps=LPS(pat)
    while i<lns and j<lnp:
        if stg[i]==pat[j]:
            i+=1
            j+=1
        else:
            if j==0:
                i+=1
            else:
                j=lps[j-1]
    if j==lnp:
        print("pattern found in the given string")
    else:
        print("pattern not found in the given string")

