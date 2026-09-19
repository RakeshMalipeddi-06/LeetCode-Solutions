class Node:
    def __init__(self,url):
        self.url=url
        self.prev=None
        self.next=None
class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        node=Node(homepage)
        self.curr=node
    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        nn=Node(url)
        self.curr.next=nn
        nn.prev=self.curr
        self.curr=nn
        
    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps>0 and self.curr.prev:
            self.curr=self.curr.prev
            steps-=1
        return self.curr.url

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps>0 and self.curr.next:
            self.curr=self.curr.next
            steps-=1
        return self.curr.url
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)