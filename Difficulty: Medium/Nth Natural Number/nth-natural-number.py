#User function Template for python3

class Solution:
    def findNth(self,n):
        #code here
        count = 0
        place = 1
        
        while n > 0:
            
            count += (n % 9) * place
            n //= 9
            place *= 10
            
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for i in range(0, t):
    n = int(input())
    obj = Solution()
    s = obj.findNth(n)
    print(s)

# } Driver Code Ends