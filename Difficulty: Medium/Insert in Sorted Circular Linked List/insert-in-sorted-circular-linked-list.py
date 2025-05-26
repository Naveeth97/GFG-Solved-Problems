
class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None

class Solution:
    def sortedInsert(self, head, data):
        #code here
        
        # three cases will occur
        # case 1 : if the data is inserted into head, then need to take care of head-tail connection.
        # case 2 : if the data is inserted into middle, then no worry use two pointer.
        # case 3 : if the data is inserted into tail, then need to take care tail-head connection.
        
        find_tail = self.find_tail(head)
        new_node = Node(data)
        
        # print("coming first")
        
        if data <= head.data:
            
            new_node.next = head
            find_tail.next = new_node
            head = new_node
            return head
            
        # print("coming second")
        
        if find_tail.data <= data:
            
            find_tail.next = new_node
            new_node.next = head
            return head
        
        prev = head
        traverse = head.next
        
        
        while traverse != head:
            
            # print("coming inside")
            
            if traverse.data <= data:
                
                prev = traverse
                traverse = traverse.next
            
            else:
                
                new_node.next = traverse
                prev.next = new_node
                break
            
                
        return head
    
    def find_tail(self, head):
        
        tail = head
        
        while (tail.next != head):
            
            tail = tail.next
            
        return tail
        
        