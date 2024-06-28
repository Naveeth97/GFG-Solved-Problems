#User function Template for python3

class Solution:
    def pattern(self, N):
        # code here
        temp = N
        lis = []
        
        if N < 0:
            lis.append(N)
            return lis
        
        while temp > 0:
            lis.append(temp)
            temp -= 5
        
        while temp != N:
            
            lis.append(temp)
            temp += 5
            
        lis.append(temp)
            
        return lis


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends