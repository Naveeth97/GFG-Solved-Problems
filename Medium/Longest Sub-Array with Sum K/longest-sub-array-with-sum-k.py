#User function Template for python3

class Solution:
    
    def find_maximum(self,value1,value2):
        if(value1>value2):
            return value1
            
        return value2
        
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        
        maxlength = 0
        sum = 0
        maps = {}
        
        for i in range(n):
            
            sum += arr[i]
            
            if(sum == k):
                maxlength = self.find_maximum(maxlength,i+1)
                
            rem = sum - k
            if(rem in maps):
                length = i - maps[rem]
                maxlength = max(maxlength, length)
                
            if(sum not in maps):
                maps[sum] = i
            
                
        return maxlength
                
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends