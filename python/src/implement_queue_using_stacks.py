class MyQueue:
    """Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all
    the functions of a normal queue (push, peek, pop, and empty).

    Implement the MyQueue class:
        - void push(int x) Pushes element x to the back of the queue.
        - int pop() Removes the element from the front of the queue and returns it.
        - int peek() Returns the element at the front of the queue.
        - boolean empty() Returns true if the queue is empty, false otherwise.

    Notes:
        - You must use only standard operations of a stack, which means only push to top, peek/pop from top,
        size, and is empty operations are valid.
        - Depending on your language, the stack may not be supported natively. You may simulate a stack using a
        list or deque (double-ended queue) as long as you use only a stack's standard operations.

    Faster than 15.88% of solutions. Less memory than 22.02% of solutions.
    """

    def __init__(self):
        """
        Initialise your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        """
        Pushes element x to the back of the queue.

        :param x: The int to be added to the queue.
        :type x: Int.
        :return: NoneType.
        :rtype: NoneType.

        The time and space complexity is O(N).
        """
        # an element at the back of the queue should be at the bottom of the stack
        # add elements from s1 to s2 in reverse order
        while self.s1:
            self.s2.append(self.s1.pop());

        # add s1 to the bottom of the stack
        self.s1.append(x)

        # add elements from s2 back to s1 in reverse order
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        """
        Returns the element at the front of the queue.
        :return: True if the queue is empty and false otherwise.
        :rtype: Bool.

        The time and space complexity is O(1).
        """
        if self.s1:
            return self.s1.pop()

    def peek(self) -> int:
        """
        Returns the element at the front of the queue.

        :return: The last element from the front of the queue.
        :rtype: Int.

        The time and space complexity is O(1).
        """
        if self.s1:
            return self.s1[-1]

    def empty(self) -> bool:
        """
        Returns the element at the front of the queue.

        :return: True if the queue is empty and false otherwise.
        :rtype: Bool.

        The time and space complexity is O(1).
        """
        return len(self.s1) == 0
