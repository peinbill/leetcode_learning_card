from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        result = []
        if root==None:
            return result
        _queue = []
        _queue.append(root)
        while len(_queue)!=0:
            node = _queue.pop(0)
            result.append(node.val)
            if node.left!=None:
                _queue.append(node.left)
            if node.right!=None:
                _queue.append(node.right)
        return result