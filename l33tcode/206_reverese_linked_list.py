# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            tmp = current.next # Store next pointer
            current.next = prev # reverse current node pointer
            prev = current # move the prev pointer to the right
            current = tmp # move the current pointer to the right
        return prev # stores the last node of the list - the new head






