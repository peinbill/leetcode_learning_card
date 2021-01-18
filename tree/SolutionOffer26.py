class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def isSameStructure(s:TreeNode,t:TreeNode):
            if t==None:
                return True
            if s==None:
                return False

            if s.val!=t.val:
                return False
            return isSameStructure(s.left,t.left) and isSameStructure(s.right,t.right)

        if B == None:
            return False
        if A == None:
            return False
        return isSameStructure(A,B ) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
