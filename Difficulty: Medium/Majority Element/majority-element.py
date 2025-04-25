#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #code here
        
        majority_element = arr[0]
        count = 1
        
        for i in range(1, len(arr)):
            
            if count == 0:
                majority_element = arr[i]
            
            if arr[i] == majority_element:
                count += 1
            else:
                count -= 1
                
        count = 0
                
        for i in range(len(arr)):
            
            if arr[i] == majority_element:
                count += 1
                
            if count > len(arr) // 2:
                return majority_element 
            
        
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
from sys import stdin


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(arr))
        print("~")
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends