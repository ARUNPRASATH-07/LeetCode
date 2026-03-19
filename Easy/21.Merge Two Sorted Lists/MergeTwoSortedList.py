class Solution(object):
    def mergeTwoLists(self, list1, list2):
        
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            
            current = current.next   # IMPORTANT

        # Attach remaining nodes
        while list1:
            current.next = ListNode(list1.val)
            list1 = list1.next
            current = current.next

        while list2:
            current.next = ListNode(list2.val)
            list2 = list2.next
            current = current.next

        return dummy.next