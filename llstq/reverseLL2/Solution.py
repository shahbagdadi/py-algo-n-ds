from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def printLL(self,node):
        while node:
            print(f' {node.val} => ', end='')
            node = node.next
        print()

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n : return head
        dummy = ListNode(0)
        dummy.next , prev = head , dummy
        for i in range(m-1):                # move m steps
            prev = prev.next
        self.printLL(prev)
        hn , tn = prev , prev.next
        prev , cur = None , prev.next
        for j in range(n+1-m):              # rotate from m to n
            cur.next , prev, cur = prev, cur, cur.next
        self.printLL(prev)
        hn.next , tn.next = prev , cur
        return dummy.next
            

s = Solution()
prev = ListNode(-1)
head = prev
for i in range(1,6):
    node = ListNode(i)
    prev.next = node
    prev = node

r = s.reverseBetween(head.next,2 ,4)
# r = head.next
while r:
    print(f' {r.val} => ', end='')
    r = r.next