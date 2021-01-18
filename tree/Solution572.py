class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isSameTree(s:TreeNode,t:TreeNode):
            if s==None and t==None:
                return True
            if s==None or t==None:
                return False
            if s.val!=t.val:
                return False
            return isSameTree(s.left,t.left) and isSameTree(s.right,t.right)
        if t==None:
            return True
        if s==None:
            return False
        return isSameTree(s,t) or self.isSubtree(s.left,t) or self.isSubtree(s.right,t)