class MinStack:
    """
    Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

    Implement the MinStack class:
        - MinStack() initializes the stack object.
        - void push(int val) pushes the element val onto the stack.
        - void pop() removes the element on the top of the stack.
        - int top() gets the top element of the stack.
        - int getMin() retrieves the minimum element in the stack.

    Faster than 99.99% of solutions. Less memory than 56.76% of solutions.

    """

    def __init__(self):
        """
        Initialise your data structure here.
        """
        self.stack = []
        # the smallest element up until each point in self.stack
        self.min_stack = []

    def push(self, val: int) -> None:
        """
         Pushes the element val onto the stack. The time and space complexity is O(1).

         :param val: The val to be added to the stack.
         :return: None
         """
        self.stack.append(val)
        min_check = self.min_stack[-1] if self.min_stack else val
        self.min_stack.append(min(val, min_check))

    def pop(self) -> None:
        """
         Removes the element on the top of the stack. The time and space complexity is O(1).

         :return: None
         """
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        """
         Gets the top element of the stack. The time and space complexity is O(1).

         :return: The top element of the stack.
         """
        return self.stack[-1]

    def getMin(self) -> int:
        """
         Retrieves the minimum element in the stack. The time and space complexity is O(1).

         :return: The minimum element in the stack
         """
        return self.min_stack[-1]
