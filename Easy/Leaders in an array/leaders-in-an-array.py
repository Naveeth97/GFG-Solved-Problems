class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        #Code here
        
        res = N-1
        count = 1
        
        for i in range(N-2,-1,-1):
            
            if(A[i]>=A[res]):
                count+=1
                res = i
                
        arr = [0] * count
        
        arr[-1] = A[-1]
        res = count - 1
        j = N-2
        while(j>=0):
            
            if(A[j]>=arr[res] and res>=0):
                res -=1
                arr[res] = A[j]
            j-=1
        return arr
        
            
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        N=int(input())
        
        A=[int(x) for x in input().strip().split()]
        obj = Solution()
        
        A=obj.leaders(A,N)
        
        for i in A:
            print(i,end=" ")
        print()
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends