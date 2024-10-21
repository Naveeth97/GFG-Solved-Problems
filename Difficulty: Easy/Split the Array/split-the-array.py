#User function Template for python3
class Solution:
	def countgroup(self,arr): 
		#Complete the function
		
		mod = 10 ** 9 + 7
		xor_result = 0
		
		for i in range(len(arr)):
		    
		    xor_result ^= arr[i]
		    
		n = len(arr)
		
		if xor_result != 0:
		    return 0
		    
		total_ways = (pow(2, n - 1, mod) - 1) % mod
		
		return total_ways



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends