# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        second = slow.next
        slow.next = None
        
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        curr = head
        second = prev

        while second:
            nxt = curr.next
            nxt2 = second.next

            curr.next = second
            second.next = nxt

            curr = nxt
            second = nxt2
