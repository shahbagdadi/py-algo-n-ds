# Definition for a binary tree node.
import sys , os 
sys.path.append(os.path.abspath('../TreeUtil'))
from util import drawtree , deserialize, serialize
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def helper(node,cur_sum):
            nonlocal cnt
            if not node : return
            cur_sum += node.val
            if cur_sum == sum : cnt += 1
            cnt += h[cur_sum - sum]
            h[cur_sum] += 1
            helper(node.left,cur_sum)
            helper(node.right,cur_sum)

        h, cur_sum , cnt = defaultdict(int),0 , 0
        helper(root,sum)
        return cnt


ip = '[10,5,-3,3,2,null,11,3,-2,null,1]'
root = deserialize(ip)
s = Solution()
ans = s.pathSum(root,8)
print(ans)
        