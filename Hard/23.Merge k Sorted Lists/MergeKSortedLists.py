class Solution(object):

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        current.next = list1 if list1 else list2

        return dummy.next


    def mergeKLists(self, lists):

        # Base cases
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        # Divide
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        # Conquer
        return self.mergeTwoLists(left, right)