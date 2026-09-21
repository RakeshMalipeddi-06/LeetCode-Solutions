class MyQueue(object):

    def __init__(self):
        self.input=[]
        self.output=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.input.append(x)
    
    def transfer(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
            
    def pop(self):
        """
        :rtype: int
        """
        self.transfer()
        return self.output.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        self.transfer()
        return self.output[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.input and not self.output
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()