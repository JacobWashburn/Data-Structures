"""Stack class creation"""
import sys

sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList as S


class Stack:
    """Create a Stack for deciding in what order things should happen. This uses FILO."""
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = S()

    def push(self, value):
        """Add to the bottom of the stack"""
        self.size += 1
        return self.storage.add_to_head(value)

    def pop(self):
        """Remove from the bottom of the stack"""
        if self.size > 0:
            self.size -= 1
        return self.storage.remove_from_head()

    def len(self):
        """Return length/size of the stack"""
        return self.size
