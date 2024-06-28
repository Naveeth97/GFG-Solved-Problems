class Solution:
    def pattern (self, arr):
        res = []
        n = len(arr)
        
        for y in range(n): # checking Rows
            left, right = 0, n-1
            
            while left <= right:
                res = [y, 'R']
                if arr[y][left] != arr[y][right]:
                    res = []
                    break
                left += 1
                right -= 1
                
            if len(res) > 0:
                return str(res[0]) + " " + res[1]
                
        for x in range(n): # Checking Columns
            top, bottom = 0, n-1
            while top <= bottom:
                res = [x, 'C']
                if arr[top][x] != arr[bottom][x]:
                    res = []
                    break
                top += 1
                bottom -= 1

            if len(res) > 0:
                return str(res[0]) + " " + res[1]
                
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends