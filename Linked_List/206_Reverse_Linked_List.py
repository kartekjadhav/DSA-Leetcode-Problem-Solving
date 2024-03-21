# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Recursive Solution
#TC - O(N)
#SC - stack space - O(N)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(node, prev):
            if not node: return prev
            nextNode = node.next
            node.next = prev
            return helper(nextNode, node)
        
        prev = None
        return helper(head,prev)
    
#Iterative Solution
#TC - O(N)
#SC - O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        curr, prev =  head, None
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev 