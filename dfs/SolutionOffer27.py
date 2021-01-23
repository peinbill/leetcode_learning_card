class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root==None:
            return root
        return self.reverse(root)

    def reverse(self,root:TreeNode):
        if root==None:
            return
        root.left,root.right=root.right,root.left
        self.reverse(root.left)
        self.reverse(root.right)