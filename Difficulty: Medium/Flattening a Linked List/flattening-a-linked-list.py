'''

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
from queue import PriorityQueue

class Solution:
    def flatten(self, root):
        #Your code here
        
        lis = PriorityQueue()
        
        trav = root
        
        while trav != None:
            
            bottom_trav = trav
            curr_next = trav.next
            
            while bottom_trav.bottom != None:
                
                lis.put(bottom_trav.data)
                bottom_trav = bottom_trav.bottom
            
            lis.put(bottom_trav.data)
            bottom_trav.bottom = curr_next
            trav.next = None
            trav = curr_next
            
        
        trav = root
        
        while trav != None:
            
            trav.data = lis.get()
            trav = trav.bottom
            
        return root
                
        