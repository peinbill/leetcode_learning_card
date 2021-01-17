from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        tmpList = []
        if root==None:
            result.append(tmpList)
            return result
        _queue = []
        _queue.append(root)
        size = 1
        while len(_queue)!=0:
            node = _queue.pop(0)
            tmpList.append(node.val)

            if node.left!=None:
                _queue.append(node.left)
            if node.right!=None:
                _queue.append(node.right)

            size-=1

            if size==0:
                result.append(tmpList.copy())
                tmpList = []
                size = len(_queue)
        return result
