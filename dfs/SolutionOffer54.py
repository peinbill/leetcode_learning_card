
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.result=[]
        self.postOrder(root)
        return self.result[k-1]
    def postOrder(self,root:TreeNode):
        if root==None:
            return
        self.postOrder(root.right)
        self.result.append(root.val)
        self.postOrder(root.left)