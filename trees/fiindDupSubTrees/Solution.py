from typing import List
import collections


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()
        ans = []
        def lookup(node):
            if node:
                key = node.val, lookup(node.left), lookup(node.right)
                uid = trees[key]
                print(f'{key} => {uid}')
                count[uid] += 1
                if count[uid] == 2:
                    ans.append(node)
                return uid

        lookup(root)
        return ans


import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize
root = deserialize('[1,2,3,4,null,2,4,null,null,4,null]')
# drawtree(root)
s = Solution()
a = s.findDuplicateSubtrees(root)
print(f'ans = {a}')
