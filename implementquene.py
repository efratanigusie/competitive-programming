class MyQueue(object):
    def __init__(self):
        self.input = []
        self.output = []


        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input.append(x)
      

        

    def pop(self):
        """
        :rtype: int
        """
        self.peek()
        return self.output.pop()

        

    def peek(self):
        """
        :rtype: int
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.input and not self.output
        
