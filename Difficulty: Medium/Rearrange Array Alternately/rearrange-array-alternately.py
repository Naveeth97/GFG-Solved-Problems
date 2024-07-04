#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        
        # Initialize index of first minimum 
    # and first maximum element
        max_idx = n - 1
        min_idx = 0
 
    # Store maximum element of array
        max_elem = arr[n-1] + 1
 
    # Traverse array elements
        for i in range(0, n) :
 
        # At even index : we have to put maximum element
            if i % 2 == 0 :
                arr[i] += (arr[max_idx] % max_elem ) * max_elem
                max_idx -= 1
 
        # At odd index : we have to put minimum element
            else :
                arr[i] += (arr[min_idx] % max_elem ) * max_elem
                min_idx += 1
 
    # array elements back to it's original form
        for i in range(0, n) :
            arr[i] = arr[i] // max_elem 


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
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends