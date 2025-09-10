# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        
        1 -> 3 -> 5 -> 

        2 -> 4
        
        """
        if not head or not head.next:
            return head

        odd, even = head, head.next
        even_first = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_first

        return head
