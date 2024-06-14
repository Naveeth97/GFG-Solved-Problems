#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        
        fir = n % 10
        sec = (n // 10)%10
        thir = n // 100
        
        res = (fir * fir * fir) + (sec * sec * sec) + (thir * thir * thir)
        
        if res == n:
            return "true"
        
        return "false"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends