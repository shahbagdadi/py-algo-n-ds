import bisect
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        def helper(lo = float('-inf'), hi = float('inf')):
            nonlocal idx
            # print(idx)
            if idx == len(preorder): 
                return None
            val = preorder[idx]
            if  val < lo or val > hi :
                return None
            idx += 1
            root = TreeNode(val)
            root.left = helper(lo, val)
            root.right = helper(val, hi)
            return root
        idx = 0 
        return helper()


s = Solution()
ip = [8,5,1,7,10,12]
root = s.bstFromPreorder(ip)
print(root.val)
import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
serialize(root)
