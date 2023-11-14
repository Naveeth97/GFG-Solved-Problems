#User function Template for python3

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        maps = {}
        
        count = 0
        
        for i in range(n):
            
            if k - arr[i] in maps:
                count += maps[k - arr[i]]
                
            if arr[i] in maps:
                maps[arr[i]] += 1
                
            else:
                maps[arr[i]] = 1
                
        return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends