class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    data = []
    length = 0

    def push(self, x):
        # write your code here
        self.data = [x] + self.data
        self.length += 1

    """
    @return: nothing
    """

    def pop(self):
        # write your code here
        # self.data = self.data[1::]

        if self.data:
            self.length -= 1
            return self.data.pop(0)
        else:
            raise IndexError("EMPYT STACK")

    """
    @return: An integer
    """

    def peek(self):
        # write your code here
        if self.data:
            return self.data[0]

    def top(self):
        # write your code here
        return self.peek()

    """
    @return: True if the stack is empty
    """

    def isEmpty(self):
        # write your code here
        return self.size == 0

    @property
    def size(self):
        return len(self.data)

    def length(self):
        return self.length
