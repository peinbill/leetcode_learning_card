
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root==None:
            return True
        return self.isSymetric2(self,root.left,root.right)

    def isSymetric2(self,p:TreeNode,q:TreeNode):
        if p.val!=q.val:
            return False
        if p==None and q==None:
            return True
        elif p==None:
            return False
        elif q==None:
            return False
        return self.isSymetric2(p.left,q.right) and self.isSymetric2(p.right,q.left)


