from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidSequence1(self, root: TreeNode, arr: List[int]) -> bool:
        def traverse(root,arr,par):
            par.append(root.val)
            if not root.left and not root.right : 
                if  arr == par : return True
            left = right = False
            if root.left: 
                left = traverse(root.left,arr,par)
                par.pop()
            if root.right:
                right = traverse(root.right,arr,par)
                par.pop()
            return  left or right
        return traverse(root,arr,[])

    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:   
        N = len(arr)
        def dfs(node, index):
            if node and node.val == arr[index]:
                index += 1
                if index == N:
                    return not node.left and not node.right
                else:
                    return dfs(node.left, index) or dfs(node.right, index)
            return False    
            
        return dfs(root, 0)

import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
root = deserialize('[0,1,0,0,1,0,null,null,1,0,0]')
# drawtree(root)
# serialize(root)

arr = [0,1,0,1]
s = Solution()
print(s.isValidSequence(root,arr))