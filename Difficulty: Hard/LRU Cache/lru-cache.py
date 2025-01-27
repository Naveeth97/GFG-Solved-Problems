#User function Template for python3

class Node:
    def __init__(self,key,value):
        self.key=key
        self.value=value
        self.next=None
        self.prev=None
        
class LRUCache:
    def __init__(self, cap):
        self.cap=cap
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head
        self.cacheMap=dict()
        
    def get(self, key):
        node=self.cacheMap.get(key,None)
        if node:
            self.deleteNode(node)
            self.insertEnd(node)
        return node.value if node else -1
        
    def put(self, key, value):
        node=self.cacheMap.get(key,None)
        if node:
            self.deleteNode(node)
            self.cacheMap.pop(key)
        newNode=Node(key,value)
        self.insertEnd(newNode)
        self.cacheMap[key]=newNode
        if len(self.cacheMap)>self.cap:
            self.cacheMap.pop(self.head.next.key)
            self.deleteNode(self.head.next)
        
    def insertEnd(self, newNode):
        self.tail.prev.next=newNode
        newNode.prev=self.tail.prev
        self.tail.prev=newNode
        newNode.next=self.tail
        
    def deleteNode(self, node):
        node.prev.next=node.next
        node.next.prev=node.prev
        
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3


def inputLine():
    return input().strip().split()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        capacity = int(input())
        cache = LRUCache(capacity)

        queries = int(input())
        for __ in range(queries):
            vec = inputLine()
            if vec[0] == "PUT":
                key = int(vec[1])
                value = int(vec[2])
                cache.put(key, value)
            else:
                key = int(vec[1])
                print(cache.get(key), end=" ")
        print()
        print("~")

# } Driver Code Ends