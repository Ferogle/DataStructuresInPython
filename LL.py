MOD = 1000000007
MOD2 = 998244353
ii = lambda: int(input())
si = lambda: input()
dgl = lambda: list(map(int, input()))
f = lambda: map(int, input().split())
il = lambda: list(map(int, input().split()))
ls = lambda: list(input())
let = 'abcdefghijklmnopqrstuvwxyz'
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def midpoint_linkedlist(head):
    tortoise=head
    hare=head.next
    while True:
        if hare==None or hare.next==None:
            break
        tortoise=tortoise.next
        hare=hare.next.next
    return tortoise

def merge(head1,head2):
    ft,fh=None,None
    it1,it2=head1,head2
    if it1.data<=head2.data:
        fh=it1
        ft=it1
        it1=it1.next
    else:
        fh=it2
        ft=it2
        it2=it2.next
    while it1!=None and it2!=None:
        if it1.data<=it2.data:
            ft.next=it1
            it1=it1.next
        else:
            ft.next=it2
            it2=it2.next
        ft=ft.next
    while it1!=None:
        ft.next=it1
        it1=it1.next
        ft=ft.next
    while it2!=None:
        ft.next=it2
        it2=it2.next
        ft=ft.next
    ft.next=None
    return fh

def mergeSort(head):
    if head==None or head.next==None:
        return head
    midpt=midpoint_linkedlist(head)
    head2=midpt.next
    midpt.next=None
    h1=mergeSort(head)
    h2=mergeSort(head2)
    hs=merge(h1,h2)
    return hs

def ll(arr):
    if len(arr)==0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head

def printll(head):
    while head:
        print(head.data, end=' ')
        head = head.next
    print()

def reverseRecursive(head):
    if head==None or head.next==None:
        return head
    currNode=reverseRecursive(head.next)
    x=head.next
    x.next=head
    head.next=None
    return currNode

def swap_nodes(head, i, j):
    if i==j:
        return head
    if i>j:
        i,j=j,i
    x,y=0,0
    px,cx,py,cy,nx,ny=None,head,None,head,None,None
    ix,iy=0,0
    while ix<i or iy<j:
        if ix<i:
            px=cx
            cx=cx.next
            ix+=1
        if iy<j:
            py=cy
            cy=cy.next
            iy+=1
    nx=cx.next
    ny=cy.next
    if i+1==j:
        cy.next=py
        py.next=ny
    else:
        cy.next=nx
        py.next=cx
        cx.next=ny
    if px:
        px.next=cy
    if i==0:
        return cy
    return head
def reverseIterative(head):
    prev=None
    curr=head
    while curr!=None:
        x=curr.next
        curr.next=prev
        prev=curr
        curr=x
    return prev
def bubbleSortLL(head):
    if head==None or head.next==None:
        return head
    curr=head
    n=0
    while curr:
        curr=curr.next
        n+=1
    for i in range(n):
        prev=None
        currHead=head
        currNext=currHead.next
        flg=1
        while currNext:
            if currHead.data>currNext.data:
                flg=0
                x=currNext.next
                currNext.next=currHead
                currHead.next=x
                if prev:
                    prev.next=currNext
                else:
                    head=currNext
                prev = currNext
                currNext = currHead.next
            else:
                prev=currHead
                currHead=currNext
                currNext=currNext.next
            temp=head
            while temp:
                print(temp.data,end=' ')
                temp=temp.next
            print()
        if flg:
            break
    return head
# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = reverseRecursive(l)
printll(l)
