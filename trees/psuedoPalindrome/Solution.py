
import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pseudoPalindromicPaths (self, root) -> int:
        self.ans , self.nset = 0 , set()
        
        def dfs(node) :
            if not node : return                
            if node.val in self.nset :
                self.nset.remove(node.val)
            else :
                self.nset.add(node.val)
            if not node.left and not node.right and len(self.nset) <= 1 :
                print(self.nset)
                self.ans += 1
            
            dfs(node.left)
            dfs(node.right)
            
        dfs(root) 
        return self.ans


s = Solution()
root = deserialize('[2,1,1,1,3,null,null,null,null,null,1]')
print(s.pseudoPalindromicPaths(root))
# print(s.isBalanced(root))
# drawtree(root)