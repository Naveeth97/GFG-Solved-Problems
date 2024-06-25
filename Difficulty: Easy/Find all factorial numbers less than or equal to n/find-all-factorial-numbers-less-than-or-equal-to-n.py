#User function Template for python3

class Solution:
    def factorialNumbers(self, n):
    	#code here 
    	lis = [1]
    	
        for i in range(2, n + 1):
            
            temp = self.factorial(i) 
            if temp <= n:
                lis.append(temp)
            else:
                break
        
        return lis
        
    def factorial(self, n):
        
        if n <= 1:
            return 1
        
        return n * self.factorial(n - 1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorialNumbers(N)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends