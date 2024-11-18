#User function Template for python3

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #Your code here
        
        d = d % len(arr)
        
        self.swap(arr, 0, d - 1)
        self.swap(arr, d, len(arr) - 1)
        self.swap(arr, 0, len(arr) - 1)
        
    
    def swap(self, arr, fir, lst):
        
        while fir < lst:
            
            arr[fir] ^= arr[lst]
            arr[lst] ^= arr[fir]
            arr[fir] ^= arr[lst]
            fir += 1
            lst -= 1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())

    while (T > 0):
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ob.rotateArr(A, D)

        for i in A:
            print(i, end=" ")

        print()

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends