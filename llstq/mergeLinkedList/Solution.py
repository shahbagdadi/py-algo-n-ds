# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        h = ListNode(0)
        n = h
        while l1 and l2:
            if l1.val < l2.val:
                n.next = l1
                l1 = l1.next
            else:
                n.next = l2
                l2 = l2.next
            n = n.next
        n.next = l1 or l2
        return h.next


s = Solution()

l1, l2, l3 = ListNode(1), ListNode(2), ListNode(3)
l1.next = l2
l2.next = l3

p1, p2, p3 = ListNode(1), ListNode(2), ListNode(4)
p1.next = p2
p2.next = p3

ans = s.mergeTwoLists(l1, p1)
while ans:
    print(f' {ans.val} = >', end='')
    ans = ans.next
