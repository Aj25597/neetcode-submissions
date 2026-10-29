# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slowie = head
        fastie = head
        while fastie is not None and fastie.next is not None:
            fastie = fastie.next
            if slowie == fastie:
                return True
            else:
                slowie = slowie.next
                fastie = fastie.next
        return False


        