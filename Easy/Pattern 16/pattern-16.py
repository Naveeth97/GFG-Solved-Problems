#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        char_val = 65
        for i in range(N):
            
            for j in range(i+1):
                print(chr(char_val),end='')
            print()
            char_val+=1
                


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