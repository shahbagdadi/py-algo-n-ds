

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        prev , cur = None , head
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev


s = Solution()
prev = ListNode(-1)
head = prev
for i in range(5):
    node = ListNode(i)
    prev.next = node
    prev = node

r = s.reverseList(head.next)
while r:
    print(f' {r.val} => ', end='')
    r = r.next
