class Node:
    """
    Definition for a doubly-linked list containing key-value pairs.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None


class LRUCache:
    """
    Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

    Implement the LRUCache class:
        - LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
        - int get(int key) Return the value of the key if the key exists, otherwise return -1.
        - void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair
          to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used
          key.

    The functions get and put must each run in O(1) average time complexity.

    Faster than 23.39% of solutions. Less memory than 48.81% of solutions.
    """

    def __init__(self, capacity: int) -> None:
        """
        Initialise the data structure.

        :param capacity: The capacity of the LRU Cache.
        :return None
        """
        self.capacity = capacity
        # cache will be the dict that contains pointers to key/value pair nodes
        self.cache = {}
        # empty pointer to least recently used key/value pair
        self.left = Node(0, 0)
        # empty pointer to most recently used key/value pair
        self.right = Node(0, 0)
        # initially they are the only nodes in the list
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node: Node) -> None:
        """
        Insert a node as the most recently used node. The time and space complexity is O(1).

        :param node: The node for insertion
        :return None
        """
        # find the end of the list
        prev = self.right.prev
        next = self.right

        # connect the new node
        prev.next = next.prev = node
        node.next = next
        node.prev = prev

    def remove(self, node: Node) -> None:
        """
        Remove a node from the list. The time and space complexity is O(1).

        :param node: The node for insertion
        :return None
        """
        # find the connecting nodes
        prev = node.prev
        next = node.next

        # remove connections from node and connect to adjacent nodes
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        """
        Get the value from the cache. The time and space complexity is O(1).

        :param key: The key associated with the value.
        :return int: The value.
        """
        if key in self.cache:
            # it needs to be removed and inserted as it is now the most recently used node
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value

        return -1

    def put(self, key: int, value: int) -> None:
        """
        Insert a key-value pair into the cache. The time and space complexity is O(1).

        :param key: The key.
        :param value: The value.
        :return None
        """
        # need to reinsert if already present
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if we exceed the capacity we drop the least recently used
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
