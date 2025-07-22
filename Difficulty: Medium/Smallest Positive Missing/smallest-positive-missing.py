class Solution:
    def missingNumber(self, arr):
        # code here
        
        # count sorting algo,
        
        n = len(arr)
        
        i = 0
        
        while i < n:
            
            if arr[i] > 0 and arr[i] <= n:
                
                if arr[i] != arr[arr[i] - 1]:
                    
                    self.swap(arr[i] - 1, i, arr)
                else :
                    i += 1
                    
            else :
                i += 1
                
        
        for i in range(len(arr)):
            
            if arr[i] - 1 != i:
                
                return i + 1
                
        return n + 1
        
    
    def swap(self, fir, sec, arr):
        
        if fir != sec:
            
            arr[fir] ^= arr[sec]
            arr[sec] ^= arr[fir]
            arr[fir] ^= arr[sec]
                
                