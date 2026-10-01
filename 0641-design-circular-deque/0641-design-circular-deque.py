class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q=[None]*k
        self.c=0
        self.f=0
        self.r=0
        self.k=k

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.c==self.k:
            return False
        self.f=(self.f-1+self.k)%self.k
        self.q[self.f]=value
        self.c=self.c+1
        return True

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.c==self.k:
            return False
        self.q[self.r]=value
        self.r=(self.r+1)%self.k
        self.c=self.c+1
        return True
        
    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.c==0:
            return False
        self.f=(self.f+1)%self.k
        self.c=self.c-1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.c==0:
            return False
        self.r=(self.r-1+self.k)%self.k
        self.c=self.c-1
        return True

    def getFront(self):
        """
        :rtype: int
        """
        if self.c==0:
            return -1
        return self.q[self.f]
        

    def getRear(self):
        """
        :rtype: int
        """
        if self.c==0:
            return -1
        ind=(self.r-1+self.k)%self.k
        return self.q[ind]
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.c==0
        

    def isFull(self):
        """
        :rtype: bool
        """
        return self.c==self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()