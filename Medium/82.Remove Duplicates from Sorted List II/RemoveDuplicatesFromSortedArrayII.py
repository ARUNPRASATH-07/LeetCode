class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        
        while curr:
            
            # detect duplicates
            if curr.next and curr.val == curr.next.val:
                
                # skip all nodes with same value
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                
                # skip last duplicate
                prev.next = curr.next
            
            else:
                # no duplicate, move prev
                prev = prev.next
            
            curr = curr.next
        
        return dummy.next