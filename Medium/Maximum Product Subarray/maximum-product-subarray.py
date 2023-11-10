#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr, n):
		# code here
		maximum_product = -2**32
		
		product = 1
		for i in range(n):
		    product *=arr[i]
		    
		    maximum_product = max(maximum_product,product)
		    
		    if(arr[i] == 0):
		        product = 1
		        
		product = 1
		        
		for i in range(n-1,-1,-1):
		    product *=arr[i]
		    
		    maximum_product = max(maximum_product, product)
		    
		    if(arr[i] == 0):
		        product = 1
		    
		    
		    
		return maximum_product
		
		
		
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends