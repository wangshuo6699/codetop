# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkList(object):
    def __init__(self):
        # 先初始化一个头节点，为None
        self.head = None

    # 链表初始化函数, 方法类似于尾插
    def initList(self, data):
        # 创建头结点
        # 这个节点创建完，包含两部分：是个既包含节点值，也包含节点所链接的下一个节点
        self.head = ListNode(data[0])

        # 初始化p指向头节点
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = ListNode(i)
            p.next = node
            # 构建完一个节点，移动到构建完的节点上，继续向后构建节点
            p = p.next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return []
        if len(lists)==1:
            return lists[0]
        dummy_head = self.mergeTwoList(lists[0], lists[1])
        for i in range(2, len(lists)):
            dummy_head = self.mergeTwoList(dummy_head, lists[i])
        return dummy_head
    
    def mergeTwoList(self, list1, list2):
        dummy_head = ListNode(None)
        cur = dummy_head
        while list1 and list2:
            while list1 and list2 and list1.val<=list2.val:
                cur.next = list1
                cur = cur.next
                list1 = list1.next
            while list1 and list2 and list1.val>list2.val:
                cur.next = list2
                cur = cur.next
                list2 = list2.next
        if list1:
            cur.next = list1
        if list2:
            cur.next = list2
        return dummy_head.next
            

l1 = LinkList()
l2 = LinkList()
l3 = LinkList()
l1.initList([1,4,5])
l2.initList([1,3,4])
l3.initList([2,6])

solution = Solution()
solution.mergeKLists([l1.head, l2.head, l3.head])
      