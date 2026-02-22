#User function Template for python3

class Solution:
    def firstNegInt(self, arr, k): 
         # code here 
         
        
        res = []
        
        queue = []
        
        for i in range(len(arr)):
            
            while queue and queue[0] <= i - k:
                
                queue.pop(0)
            
            if arr[i] < 0:
                
                queue.append(i)
                
            if queue and i + 1 >= k:
                res.append(arr[queue[0]])
            elif i + 1 >= k:
                res.append(0)
                
        return res
        
