#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(2*N-1):
            
            for j in range(2*N-1):
                top = i
                bottom = j
                right = (2*N - 2) - j;
                left = (2*N - 2) - i;
                
                print(N - min(min(top,bottom), min(left,right)), end = " ");
            print()



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends