#User function Template for python3
class Solution:
    def sumClosest(self, arr, target):
        # code here
        
        n = len(arr)
        
        if n < 2:
            return []
            
        arr.sort()
        
        closest = (1 << 31)
        
        left = 0
        right = len(arr) - 1
        
        pairs = [0, 0]
        
        while left < right:
            
            sum = arr[left] + arr[right]
            
            if closest > abs(sum - target):
                closest = abs(sum - target)
                pairs[0] = arr[left]
                pairs[1] = arr[right]
            
            if sum > target:
                right -= 1
            else:
                left += 1
                
        return pairs
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())
    while t > 0:
        arr = list(map(int, input().strip().split()))
        target = int(input().strip())
        ob = Solution()
        ans = ob.sumClosest(arr, target)
        if not ans:
            print("[]")
        else:
            print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends