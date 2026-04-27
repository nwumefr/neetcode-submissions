# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        over = 0
        while l1 != None and l2 != None:
            val = l1.val + l2.val + over
            if val>9:
                over = 1
                val = val%10
            else:
                over = 0
            print(val,over)
            nodes.append(ListNode(val=val,next=None))
            l1 = l1.next
            l2 = l2.next
            print(nodes)
        left_over = None
        if l1!=None and l2==None:
            left_over = l1
        elif l1==None and l2!=None:
            left_over = l2
        while left_over!=None:
            val = left_over.val + over
            if val>9:
                over = 1
                val = val%10
            else:
                over = 0
            print(val,over)
            nodes.append(ListNode(val=val,next=None))
            left_over = left_over.next

        if over!=0:
            nodes.append(ListNode(val=over,next=None))
        _len = len(nodes)
        for i in range(_len):
            if i != _len - 1:
                nodes[i].next = nodes[i+1]
        return nodes[0]