
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root:
            return
        # we always want to delete the node when it is the root of a subtree,
        # so we handle left or right according to the val.
        # if the node does not exist, we will hit the very first if statement and return None.
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # now the key is the root of a subtree
        else:
            # if the subtree does not have a left child, we just return its right child
            # to its father, and they will be connected on the higher level recursion.
            if not root.left:
                return root.right
            
            # if it has a left child, we want to find the max val on the left subtree to 
            # replace the node we want to delete.
            else:
                # try to find the max value on the left subtree
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                    
                # replace
                root.val = tmp.val
                
                # since we have replaced the node we want to delete with the tmp, now we don't
                # want to keep the tmp on this tree, so we just use our function to delete it.
                # pass the val of tmp to the left subtree and repeat the whole approach.
                root.left = self.deleteNode(root.left, tmp.val)
        
        return root


import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize
root = deserialize('[5,3,6,2,4,null,7]')

s = Solution()
r = s.deleteNode(root,3)
drawtree(r)