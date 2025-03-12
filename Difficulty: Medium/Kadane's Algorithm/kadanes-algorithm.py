class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        
        maxEnd = arr[0]
        maxSoFar = arr[0]
        
        for i in range(1, len(arr)):
            
            maxEnd = max(arr[i], maxEnd + arr[i])
            maxSoFar = max(maxSoFar, maxEnd)
            
        return maxSoFar

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends