#User function Template for python3
class Solution:
    #Complete this function
    # Function to find the maximum index difference.
    def maxIndexDiff(self,A, N): 
        ##Your code here
        arr = [0]*N
        arr[0] = A[0]
        for i in range(1,N):
            arr[i] = min(arr[i-1],A[i])
            
        maxi = -2**32
        i = N-1
        j = N-1
        while(i>=0 and j>=0):
            if(A[j]>=arr[i]):
                maxi = max(maxi,j-i)
                i-=1
            else:
                j-=1
        return maxi




#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends