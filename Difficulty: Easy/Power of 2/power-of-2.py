#User function Template for python3

class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n : int ) -> bool:
        ##Your code here
        
        if (n == 0):
            return False
        
        if (n & (n - 1) == 0):
            
            return True
            
        return False





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        n = int(input())
        ob = Solution()
        if ob.isPowerofTwo(n):
            print("true")
        else:
            print("false")

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends