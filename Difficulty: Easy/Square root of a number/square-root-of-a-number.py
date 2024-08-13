#User function Template for python3


#Complete this function
class Solution:
    def floorSqrt(self, n): 
    #Your code here
    
        low, high = 1, n
        res = 0
    
        while low <= high:
        
            mid = (low + high) //2
        
            if (mid * mid <= n):
                res = low
                low = mid + 1
            else:
                high = mid - 1
        
        return high 
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        x = int(input())

        print(Solution().floorSqrt(x))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends