from typing import List
import sys

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(cur):
            prev = None
            while cur :
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp
            return prev

        slow = fast = head
        new_head , prevk_head = None , None
        while fast:
            for i in range(k-1):
                if fast.next :
                    fast = fast.next
                else:
                    prevk_head.next = fast_tail
                    return new_head
            if not new_head : new_head = fast
            fast_tail , fast.next = fast.next , None
            thisk_head = reverse(slow)
            if prevk_head :
                prevk_head.next = thisk_head
            prevk_head = slow
            slow = fast = fast_tail
        return new_head

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
ans = s.reverseKGroup(l1, 3)
# ans = l1
while ans:
    print(ans.val)
    ans = ans.next