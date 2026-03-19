# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            # Get the values of the current nodes, if they exist
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of the current digits and the carry
            total = val1 + val2 + carry
            carry = total // 10
            digit = total % 10
            
            # Create a new node with the calculated digit
            current.next = ListNode(digit)
            current = current.next
            
            # Move to the next nodes in the lists, if they exist
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                
        return dummy_head.next