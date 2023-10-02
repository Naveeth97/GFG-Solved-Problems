#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        
        for i in range(N):
            char_val = 65 + (N-1)
            for j in range(i+1):
                print(chr(char_val),end=' ')
                char_val -=1
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