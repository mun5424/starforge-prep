# collect all the leaf nodes until the tree is empty.
import collections
from typing import Collection, List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findLeaves(self, root: 'TreeNode') -> List[str]:
        res = collections.defaultdict(list) 
        
        def dfs(node, layer):
            if not node:
                return layer

            left = dfs(node.left, layer)
            right = dfs(node.right, layer) 

            layer = max(left, right) 
            res[layer].append(node.val) 
            return layer + 1
        dfs(root, 0) 

        return res.values() 



sol = Solution() 
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(sol.findLeaves(root)) # [[4, 5, 6], [2, 3], [1]]