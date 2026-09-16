class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        old_to_new = {}

        # 1. Create a copy of every node
        curr = head

        while curr:
            old_to_new[curr] = Node(curr.val)
            curr = curr.next

        # 2. Connect next and random pointers
        curr = head

        while curr:
            copy = old_to_new[curr]

            copy.next = old_to_new.get(curr.next)
            copy.random = old_to_new.get(curr.random)

            curr = curr.next

        return old_to_new[head]