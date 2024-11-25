#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		
		n = len(arr)
		max_prod = arr[0]
		min_prod = arr[0]
		result = arr[0]
		
		for i in range(1, n):
		    
		    if arr[i] < 0:
		        max_prod, min_prod = min_prod, max_prod
		        
		    max_prod = max(arr[i], max_prod * arr[i])
		    min_prod = min(arr[i], min_prod * arr[i])
		    
		    result = max(result, max_prod)
		    
	    return result

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends