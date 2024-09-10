#User function Template for python3

class Solution:
    def singleElement(self, arr, N):
        # code here 
        
        #brute force solution
        
        maps = {}
        
        for i in arr:
            
            if i not in maps:
                maps[i] = 0
                
            maps[i] += 1
            
        for i in arr:
            
            if maps[i] == 1:
                
                return i
                
        return -1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.singleElement(arr,N))
# } Driver Code Ends