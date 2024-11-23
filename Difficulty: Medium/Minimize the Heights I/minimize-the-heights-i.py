#User function Template for python3

class Solution:
    def getMinDiff(self,k, arr):
        # code here
        
        arr.sort()
        n = len(arr)
        
        res = arr[len(arr) - 1] - arr[0]
        maxi = 0
        mini = 0
        
        for i in range(1, len(arr)):
            
            maxi = max(arr[n - 1] - k, arr[i - 1] + k)
            mini = min(arr[0] + k, arr[i] - k)
            
            res = min(res, maxi - mini)
            
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.getMinDiff(k, arr)
        print(res)
        print("~")

# } Driver Code Ends