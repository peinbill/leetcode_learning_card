# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution19:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre_ = head
        pre = head
        post = head
        # post 比 pre 快n步
        for n in range(n):
            post = post.next

        # 要考虑删除head
        while not post is None:
            if pre==head:
                post = post.next
                pre = pre.next
            else:
                pre_ = pre_.next
                post = post.next
                pre = pre.next
        if pre==head:
            head = head.next
        else:
            pre_.next = pre.next
        return head

    def removeNthFromEnd2(self, head: ListNode, n: int) -> ListNode:
        Node = ListNode(None)
        Node.next = head
        first,slow = Node,Node
        for i in range(n):
            first = first.next
        while first.next != None:
            first = first.next
            slow = slow.next
        slow.next = slow.next.next
        return Node.next