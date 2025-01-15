# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        
        mpp = {}
        
        longest_subarray = 0
        
        sum = 0
        
        for i in range(len(arr)):
            
            sum += arr[i]
            
            if sum == k:
                longest_subarray = max(longest_subarray, i + 1)
                
            if sum - k in mpp:
                
                longest_subarray = max(longest_subarray, i - mpp[sum - k])
                
            if sum not in mpp:
                
                mpp[sum] = i
                
        return longest_subarray
            
            
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        tc -= 1
        print("~")
# } Driver Code Ends