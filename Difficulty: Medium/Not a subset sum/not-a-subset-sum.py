#User function Template for python3

class Solution:
    def findSmallest(self, arr):
        # code here
        ans = 1
        for i in arr:
            
            if i <= ans:
                ans += i
            else:
                break
            
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findSmallest(arr)
        print(ans)


if __name__ == "__main__":
    main()

# } Driver Code Ends