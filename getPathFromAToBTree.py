"""
given a binary tree, get path from node A to node B.
for example: 

							4
						/      \
					3            6
				/    \         /   \
			  1     9       11    4
			 /              /  \
			13            19    12

from node 1 to node 11 would be:
[up, up, right, left]

"""

# approach is finding the LCA - then finding the path from node A to that LCA, path from node B to that LCA, add them together. 


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, p, q):
            if root == p or root == q:
                return root
            left = None
            right = None 
            if root.left:
                left = lca(root.left, p, q) 
            if root.right:
                right = lca(root.right, p, q) 
                
            if left and right:
                return root
            
            return left or right 
        
        return lca(root, p, q)

    def getPath(self, root: 'TreeNode', arr: List, node: 'TreeNode') -> bool:
        if not root:
            return False
        if root == node:
            return True
        arr.append("LEFT")
        if self.getPath(root.left, arr, node):
            return True
        arr.pop()
        arr.append("RIGHT")
        if self.getPath(root.right, arr, node):
            return True
        arr.pop() 
        return False 

    def getPathFromAToB(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> List:
        lcAncestor = self.lowestCommonAncestor(root, p, q)
        startPath, destPath = [], [] 
        self.getPath(lcAncestor, startPath, p) 
        self.getPath(lcAncestor, destPath, q) 
        res = [] 
        for _ in startPath:
            res.append('UP') 
        for s in destPath: 
            res.append(s) 
        
        return res 



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
startNode = TreeNode(4)
root.left.left = startNode
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
destNode = TreeNode(7)
root.right.right = destNode


solution = Solution()
print( solution.getPathFromAToB(root, startNode, destNode)  )
