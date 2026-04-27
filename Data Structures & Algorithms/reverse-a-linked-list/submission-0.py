# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr!=None:
            temp = curr
            temp = temp.next
            print(curr,curr.next,prev,temp)
            curr.next = prev
            prev = curr
            if temp==None:
                break
            curr = temp
            print(curr,curr.next,prev,temp)
            print("-")

        print(curr)
        return curr