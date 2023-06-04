"""
tree traversal - preorder, postorder, and inorder 
For Inorder, you traverse from the left subtree to the root then to the right subtree.
For Preorder, you traverse from the root to the left subtree then to the right subtree.
For Post order, you traverse from the left subtree to the right subtree then to the root.
"""

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val 
        self.left = None
        self.right = None

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

def preorder(root):
    if not root:
        return
    print(root.val) 
    preorder(root.left)
    preorder(root.right)

def postorder(root):
    if not root:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.val) 
    