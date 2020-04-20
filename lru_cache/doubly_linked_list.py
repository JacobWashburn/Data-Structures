
class ListNode:
    """Each ListNode holds a reference to its previous node
    as well as its next node in the List."""
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def insert_after(self, value):
        """Wrap the given value in a ListNode and insert it
            after this node. Note that this node could already
            have a next node it is point to."""
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    def insert_before(self, value):
        """Wrap the given value in a ListNode and insert it
            before this node. Note that this node could already
            have a previous node it is point to."""
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    def delete(self):
        """Rearranges this ListNode's previous and next pointers
            accordingly, effectively deleting this ListNode."""
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


class DoublyLinkedList:
    """Our doubly-linked list class. It holds references to
    the list's head and tail nodes."""
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def get_node(self, value):
        """Finds a node based on it's value"""
        current = self.head
        while current.value != value:
            current = current.next
        return current

    def add_to_head(self, value):
        """Add a new node to the head of the list and assign prev attr of
        existing head to new head node.
        """
        new_head = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_head
            self.tail = new_head
        else:
            new_head.next = self.head
            self.head.prev = new_head
            self.head = new_head
        return new_head

    def remove_from_head(self):
        """Remove the current head and assign new head
        """
        self.head.delete()
        self.head = self.head.next
        if self.length > 0:
            self.length -= 1

    def add_to_tail(self, value):
        """Add a new node to the tail of the cache"""
        new_tail = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail.prev = self.tail
            self.tail.next = new_tail
            self.tail = new_tail

    def remove_from_tail(self):
        """Remove current tail and assign new tail"""
        self.tail.delete()
        self.tail = self.tail.prev
        if self.length > 0:
            self.length -= 1


    def move_to_front(self, node):
        """Move node to head of list"""
        if node is self.head:
            return
        self.add_to_head(node.value)
        node.delete()

    def move_to_end(self, node):
        """Move node to tail of list"""
        if node is self.tail:
            return
        self.add_to_tail(node.value)
        node.delete()

    def delete(self, node):
        """Delete given node from the list"""
        if self.length > 0:
            self.length -= 1
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    def get_max(self):
        """Get the max"""
        current = self.head
        max = self.head.value
        while current is not None:
            if current.value > max:
                max = current.value
            current = current.next
        return max
