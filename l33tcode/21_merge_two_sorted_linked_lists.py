# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return None
        elif list1 is None and not list2 is None:
            return list2
        elif list2 is None and not list1 is None:
            return list1
        else:
            print("List_1:",list1)
            print("List_2:",list2)
            solution = current = ListNode() # Avoid inserting in an empty list - we will return solution.next

            while list1 and list2:
                if list1.val < list2.val:
                    current.next = list1
                    list1 = list1.next
                else:
                    current.next = list2
                    list2 = list2.next
                current = current.next
            current.next = list1 or list2 # If one the lists is longer than the other
            print("Solution:", solution)
            return solution.next


                
            
            
        

