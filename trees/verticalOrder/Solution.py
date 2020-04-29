from typing import List
import collections
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        min_order , max_order = math.inf , -math.inf
        
        def traverse(root, order=0, level=0):
            nonlocal min_order , max_order
            if not root : return
            if root.left :
                traverse(root.left, order-1, level + 1)
            if root.right :
                traverse(root.right, order+1, level + 1)
            order_dict[order].append((level,root.val))
            min_order = min(min_order, order)
            max_order = max(max_order, order)

        order_dict = collections.defaultdict(list)
        traverse(root)
        # print(order_dict)
        ans = []
        for i in range(min_order,max_order+1):
            lst = [ n[1] for n in  sorted(order_dict[i])]
            ans.append(lst)
        return ans





import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
root = deserialize('[1,2,3,4,5,6,7]')
# drawtree(root)
# serialize(root)


s = Solution()
ans = s.verticalTraversal(root)
print(ans)