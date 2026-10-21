# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast, slow = head.next, head
        if not fast:
            return False
        while fast != slow:
            if fast == None or fast.next == None:
                return False
            fast = fast.next.next
            slow = slow.next
        return True
        