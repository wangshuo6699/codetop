# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_head = ListNode()
        cur = dummy_head
        while list1 and list2:
            if list1.val>=list2.val:
                cur.next=list2
                list2 = list2.next
            else:
                cur.next=list1
                list1 = list1.next
            cur = cur.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return dummy_head.next

n1 = ListNode(4)
n2 = ListNode(2, n1)
n3 = ListNode(1, n2)

n4 = ListNode(4)
n5 = ListNode(3, n4)
n6 = ListNode(1, n5)

solution = Solution()
solution.mergeTwoLists(n3, n6)
