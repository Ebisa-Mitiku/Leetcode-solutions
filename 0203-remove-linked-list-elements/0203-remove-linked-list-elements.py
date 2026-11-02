# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:

        temp=head
        prevous=None
        
        while temp is not None:

            if temp.val==val:
                if prevous is not None:
                    prevous.next=temp.next
                else:
                   head=head.next
            else:
                prevous=temp
            temp=temp.next
                

        return head
        