"""Queue Class initialization"""
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList as Q


class Queue:
    """Create a Queue"""
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = Q()

    def enqueue(self, value):
        """Add to the back of the Queue."""
        self.size += 1
        return self.storage.add_to_head(value)

    def dequeue(self):
        """Remove from the front of the Queue."""
        # Don't decrement size if 0 or less
        if self.size > 0:
            self.size -= 1
        return self.storage.remove_from_tail()

    def len(self):
        """Return the size/length of our Queue."""
        return self.size

    def q_length(self):
        """Return length of storage. It should match self.size."""
        return len(self.storage)
