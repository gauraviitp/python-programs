class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node):
        last = self.tail.prev

        last.next = node
        node.next = self.tail

        node.prev = last
        self.tail.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev


class LRUCache:

    # Constructor for initializing the cache capacity with the given value.
    def __init__(self, cap):
        self.d = {}
        self.ll = LinkedList()
        self.cap = cap

    # Function to return value corresponding to the key.
    def get(self, key):
        if key in self.d:
            node = self.d[key]
            self.ll.remove(node)
            self.ll.append(node)
            return node.val

        return -1

    # Function for storing key-value pair.
    def set(self, key, value):
        if key not in self.d:
            node = Node()
            node.key = key
            self.d[key] = node
        else:
            node = self.d[key]
            self.ll.remove(node)

        node.val = value

        self.ll.append(node)

        if len(self.d) > self.cap:
            first = self.ll.head.next
            self.ll.remove(first)
            del self.d[first.key]


cache = LRUCache(2)
cache.set(1, 2)
print(cache.get(1))
