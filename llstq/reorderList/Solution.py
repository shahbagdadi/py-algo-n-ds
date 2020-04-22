from typing import List
import sys
from collections import deque

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def printll(self , node):
        while node :
            print(f' {node.val} => ', end='')
            node = node.next

    def reorderList(self, head: ListNode) -> None:
        if not head : return
        # find the middle of LL
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse the second half of the list
        curr , prev = slow , None 
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # merge two linked list
        head1 , head2 = head, prev 
        while head2.next:
            tmp1 = head1.next
            head1.next = head2
            head1 = tmp1

            tmp2 = head2.next
            head2.next = head1
            head2 = tmp2    

        # self.printll(head)
        return 

    
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

s = Solution()
s.reorderList(l1)
ans = l1
while ans:
    print(f' {ans.val} => ', end='')
    ans = ans.next