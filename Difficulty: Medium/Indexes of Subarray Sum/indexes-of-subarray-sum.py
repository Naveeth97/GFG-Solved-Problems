#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        
        left, right = 0, 0
        sum = 0
        
        while right < len(arr):
            
            sum += arr[right]
            
            while sum > target:
                
                sum -= arr[left]
                left += 1
            
            if sum == target:
                return [left + 1, right + 1]
                
            right += 1
            
        return [-1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends