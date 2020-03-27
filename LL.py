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


def reverseIterative(head):
    prev=None
    curr=head
    while curr!=None:
        x=curr.next
        curr.next=prev
        prev=curr
        curr=x
    return prev
# Main
# Read the link list elements including -1
arr=list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = reverseRecursive(l)
printll(l)
