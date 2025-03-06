# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while(head is not None and head.next is not None):
            track1 = head
            track2 = head.next

            track1.next = track2.next
            track2.next = track1
            
            prev.next = track2
            prev = track1
            
            head = track1.next
            
        return dummy.next
        
