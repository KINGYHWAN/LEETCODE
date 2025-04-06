# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None  # 노드가 1개일 경우

        slow = head
        fast = head
        prev = None

        # fast는 2칸씩, slow는 1칸씩 이동
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        # 가운데 노드 제거
        prev.next = slow.next
        return head

