#User function Template for python3

class Solution:
	def min_operations(self,nums):
		# Code here
		n = len(nums)
		
		if(n == 1):
		    return 0
		LIS = [0 for i in range(n)]
        lens = 0
 
    # Mark all elements of LIS as 1
        for i in range(n):
            LIS[i] = 1
 
    # Find LIS of array
        for i in range(1, n):
         
            for j in range(i):
                if (nums[i] > nums[j] and (i-j)<=(nums[i]-nums[j]) ):
                    LIS[i] = max(LIS[i], LIS[j] + 1)
                 
            lens = max(lens, LIS[i])
 
    # Return min changes for array
    # to strictly increasing
        return (n - lens)
		            
		        
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution();
		ans = ob.min_operations(nums)
		print(ans)
# } Driver Code Ends