#User function Template for python3
import math
class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 

    def rotateArr(self,A,D):
        #Your code here
        N = len(A)
        D = D%N
        loop = math.gcd(D,N)
        for i in range(loop):
            j = i
            temp = A[i]
            while 1:
                k = j+D
                if(k>=N):
                    k = k - N
                if(k == i):
                    break
                A[j] = A[k]
                j = k
            A[j] = temp
        return A




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


if __name__ == "__main__":
    main()

# } Driver Code Ends