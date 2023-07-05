# collect all the leaf nodes until the tree is empty.
from typing import Collection, List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findLeaves(self, root: 'TreeNode') -> List[str]:
        res = Collection.defaultdict(list) 
        
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


