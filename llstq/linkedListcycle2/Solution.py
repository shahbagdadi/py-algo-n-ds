class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow, fast = head, head.next
        while slow is not fast:
            slow = slow.next
            if fast and fast.next:
                fast = fast.next.next
            else:
                return None
        slow, fast = head, fast.next
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


s = Solution()
lst = [3, 2, 0, -4]
# lst = [1, 2]
prev = ListNode(0)
nodes = []
for i, n in enumerate(lst):
    node = ListNode(n)
    prev.next = node
    nodes.append(node)
    prev = node
nodes[3].next = nodes[1]

print(s.detectCycle(nodes[0]).val)
