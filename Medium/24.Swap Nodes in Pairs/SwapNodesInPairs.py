# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy=ListNode(0)
        dummy.next=head
        prev=dummy

        prev=dummy
        while prev.next and prev.next.next:
            first=prev.next
            sec=first.next
            #swap
            first.next=sec.next
            sec.next=first
            prev.next=sec

            prev=first
        return dummy.next