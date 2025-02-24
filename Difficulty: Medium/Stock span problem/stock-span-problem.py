#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def calculateSpan(self, arr):
        n=len(arr)
        ans=[]
        stack=[]
        for i in range(n):
            while stack and arr[stack[-1]]<=arr[i]:
                stack.pop()
            ans.append(i-stack[-1] if stack else i+1)
            stack.append(i)
        return ans

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends