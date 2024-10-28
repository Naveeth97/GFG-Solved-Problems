#User function Template for python3

class Solution:
    #Complete this function
    def power(self,N,R):
        #Your code here
        mod = 1000000007
        
        return self.helper(N, R) % mod
        
    def helper(self, N, R):
        
        mod = 1000000007
        
        #base condition
        if R == 1:
            return N % mod
            
        if R % 2 != 0:
            
            ans = self.helper(N, R // 2)
            
            return (N * ans * ans) % mod
            
        ans = self.helper(N, R // 2)
            
        return (ans * ans) % mod
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
    
    T=int(input())
    
    while(T>0):
        
        N=input()
        R=N[::-1]
        
        ob=Solution();
        ans=ob.power(int(N),int(R))
        print(ans)
        
        T-=1

        print("~")
if __name__=="__main__":
    main()
# } Driver Code Ends