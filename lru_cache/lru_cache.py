"""LRUCache class creation"""

from doubly_linked_list import DoublyLinkedList as C


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit = 10):
        self.size = 0
        self.limit = limit
        self.storage = C()
        self.hash = {}

    def get(self, key):
        """
            Retrieves the value associated with the given key. Also
            needs to move the key-value pair to the end of the order
            such that the pair is considered most-recently used.
            Returns the value associated with the key or None if the
            key-value pair doesn't exist in the cache.
            """
        if key in self.hash:
            self.storage.move_to_front(self.hash[key])
            return self.hash[key].value
        else:
            return None

    def set(self, key, value):
        """
            Adds the given key-value pair to the cache. The newly-
            added pair should be considered the most-recently used
            entry in the cache. If the cache is already at max capacity
            before this entry is added, then the oldest entry in the
            cache needs to be removed to make room. Additionally, in the
            case that the key already exists in the cache, we simply
            want to overwrite the old value associated with the key with
            the newly-specified value.
            """
        node = None
        if key in self.hash:
            node = self.hash[key]
            node.value = value
            self.hash[key] = node
        else:
            node = self.storage.add_to_head(value)
            self.hash[key] = node
        if self.storage.length > self.limit:
            tail_value = self.storage.remove_from_tail()
            for i, v in self.hash.items():
                if self.hash[i].value == tail_value:
                    self.hash.pop(i)
                    break
        return node
