MOD = 1000000007
ii = lambda : int(input())
si = lambda : input()
dgl = lambda : list(map(int, input()))
f = lambda : map(int, input().split())
il = lambda : list(map(int, input().split()))
ls = lambda : list(input())
#  Priority Queue implementation
# when all elements are popped then its heap sort
class PQ:
    pq=[]
    def isEmpty(self):
        return len(self.pq)==0
    def getMin(self):
        return "Queue is empty" if self.isEmpty() else self.pq[0]
    def getSz(self):
        return len(self.pq)
    def insert(self,val):
        self.pq.append(val)
        CI=len(self.pq)-1
        while CI>0:
            PI=(CI-1)//2
            if self.pq[PI]>self.pq[CI]:
                self.pq[CI],self.pq[PI]=self.pq[PI],self.pq[CI]
            else:
                break
            CI=PI
    def removeMin(self):
        self.pq[0]=self.pq[-1]
        self.pq.pop(-1)
        pi=0
        lci,rci=2*pi+1,2*pi+2
        while lci<len(self.pq):
            mi=pi
            if self.pq[lci]<self.pq[mi]:
                mi=lci
            if rci<len(self.pq) and self.pq[rci]<self.pq[mi]:
                mi=rci
            if pi==mi:
                break
            self.pq[mi],self.pq[pi]=self.pq[pi],self.pq[mi]
            pi = mi
            lci, rci = 2 * pi + 1, 2 * pi + 2
l=PQ()
l.insert(20)
l.insert(30)
l.insert(10)
l.insert(5)
print(*l.pq)
l.removeMin()
print(*l.pq)
