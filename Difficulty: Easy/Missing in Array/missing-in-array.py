class Solution:
    def missingNum(self, arr):
        # code here
        
        # cyclic sort pattern
        
        i = 0
        n = len(arr)
        
        while i < n:
            
            correct = arr[i] - 1
            
            if arr[i] <= n and arr[i] != arr[correct]:
                self.swap(i, correct, arr)
            
            else:
                i += 1
                
        i = 0
        
        while i < n:
            
            if arr[i] != i + 1:
                
                return i + 1
                
            i += 1
                
        return len(arr) + 1
                
        
    def swap(self, fir, sec, arr):
        
        if fir != sec:
            
            arr[fir] ^= arr[sec]
            arr[sec] ^= arr[fir]
            arr[fir] ^= arr[sec]
        
        
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNum(arr)
    print(s)

    print("~")
# } Driver Code Ends