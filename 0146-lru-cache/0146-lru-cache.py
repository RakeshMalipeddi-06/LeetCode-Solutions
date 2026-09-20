class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.cache={}

        self.head=Node(0,0)
        self.tail=Node(0,0)
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def remove(self,node):
        pn=node.prev
        nn=node.next
        pn.next=nn
        nn.prev=pn

    def insert_after_head(self,node):
        fn=self.head.next

        node.prev=self.head
        node.next=fn
        self.head.next=node
        fn.prev=node
    
    def move_to_head(self,node):
        self.remove(node)
        self.insert_after_head(node)
    
    def pop_tail(self):
        ln=self.tail.prev
        self.remove(ln)
        return ln

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        node=self.cache[key]
        self.move_to_head(node)
        return node.value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node=self.cache[key]
            node.value=value
            self.move_to_head(node)
            return
        node=Node(key,value)
        self.cache[key]=node
        self.insert_after_head(node)

        if len(self.cache)>self.capacity:
            ln=self.pop_tail()
            del self.cache[ln.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)