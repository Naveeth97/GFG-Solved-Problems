#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N):
            
            if(i == 0 or i == N-1):
                
                for _ in range(N):
                    print('*',end='')
                
                    
            else:
                
                for _ in range(1):
                    print('*',end='')
                    
                for _ in range(N-2):
                    print(' ',end='')
                    
                for _ in range(1):
                    print('*',end='')
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