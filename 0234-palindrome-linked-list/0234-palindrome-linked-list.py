# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        n=0
        temp=head
        while temp!=None:
            n+=1
            temp=temp.next
        if n==1:
            return True
        first=[]
        second=[]

        temp=head
        x=0
        f=False
        if n%2:
            f=True
        while temp!=None:
            x+=1
            if f and x==(n+1)//2:
                second.append(temp.val)

            if x<=(n+1)//2:
                first.append(temp.val)
            else:
                second.append(temp.val)
           
            temp=temp.next   
           
        return first[::-1]==second