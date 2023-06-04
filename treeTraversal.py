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

def postorderIterative(root): 
    
    if not root: 
        return None

    stack = []

    while(True):
        while(root):
            if root.right is not None:
                stack.append(root.right) 
            stack.append(root) 

            root = root.left
        root = stack.pop()
        if root.right is not None and stack[-1] == root.right:
            stack.pop()
            stack.append(root) 
            root = root.right 
        else:
            print(root)
            root = None
        
        if len(stack) <= 0:
            break

    
    