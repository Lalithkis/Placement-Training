class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        length = 1
        current = head
        while current.next:
            current = current.next
            length += 1
        current.next = head
        k = k % length
        if k == 0:
            current.next = None
            return head
        steps_to_new_head = length - k
        new_end = head
        for _ in range(steps_to_new_head - 1):
            new_end = new_end.next
        new_head = new_end.next
        new_end.next = None
        return new_head
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
def print_linked_list(head):
    vals = []
    current = head
    while current:
        vals.append(current.val)
        current = current.next
    print(vals)
solution = Solution()
head = create_linked_list([1, 2, 3, 4, 5])
k = 2
new_head = solution.rotateRight(head, k)
print_linked_list(new_head)  # Output: [4, 5, 1, 2, 3]
head = create_linked_list([0, 1, 2])
k = 4
new_head = solution.rotateRight(head, k)
print_linked_list(new_head) 
