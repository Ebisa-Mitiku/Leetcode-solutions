# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # result=[]
        
        # temp=head
        # while temp is not None:
        #     result.append(temp.val)
        #     temp=temp.next
        # result.reverse()
        
        # temp=head
        # i=0
        # while temp is not None:
        #     temp.val=result[i]
        #     temp=temp.next
        #     i+=1
        # return head
        prev=None
        curr=head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        return prev
        