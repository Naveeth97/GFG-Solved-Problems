class Solution:
    def findMaxDiff(self, arr):
        # code here
        
        stack = [0]
        
        ls = [0] * len(arr)
        
        
        rs = [0] * len(arr)
        
        for i in range(len(arr)):
            
            while stack[-1] >= arr[i]:
                stack.pop()
                
            ls[i] = stack[-1]
            
            stack.append(arr[i])
            
        stack = [0]
        
        for i in range(len(arr) - 1, -1, -1):
            
            while stack[-1] >= arr[i]:
                
                stack.pop()
                
            rs[i] = stack[-1]
            
            stack.append(arr[i])
            
        max_abs = -2 ** 32
        
        for i in range(len(ls)):
            
            max_abs = max(max_abs, abs(ls[i] - rs[i]))
            
        return max_abs
            
            


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends