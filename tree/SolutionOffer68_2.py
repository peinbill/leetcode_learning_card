# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(root ,node):
            if root==None:
                return False
            if root.val == node.val:
                return True
            return search(root.left,node) or search(root.right,node)

        if p==root or q==root:
            return root
        if search(root.right,p) and search(root.right,q):
            return self.lowestCommonAncestor(root.right,p,q)
        elif search(root.left,p) and search(root.left,q):
            return self.lowestCommonAncestor(root.left,p,q)
        else:
            return root

    def lowestCommonAncestor12(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p==root or q==root or root==None:
            return root
        left = self.lowestCommonAncestor1(root.left,p,q)
        right = self.lowestCommonAncestor1(root.right,p,q)
        if left==None:
            return right
        elif right==None:
            return left
        else:
            return root