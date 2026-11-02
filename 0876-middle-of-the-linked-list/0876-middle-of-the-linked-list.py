# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        count=0
        temp=head
        while temp:
            count+=1
            temp=temp.next
        
        count//=2

        ind=0
        curr=head
        while curr:
            ind+=1
            if ind>count:
                head=curr
                break
            curr=curr.next
        return head

        