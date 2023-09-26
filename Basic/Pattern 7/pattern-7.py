#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code her
        for i in range(N):
            
            #leading space
            for _ in range(N-i-1):
                print(" ",end='')
                
            for _ in range(2*i+1):
                print('*',end='')
                
            #trailing space
            for _ in range(N-i-1):
                print(" ",end='')
            print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends