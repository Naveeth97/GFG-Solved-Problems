#User function Template for python3

class Solution:
	def singleNumber(self, nums):
		# Code here
		
		xor = 0
		
		for i in nums:
		    
		    xor ^= i
		    
		first_set_bit = (xor & xor - 1) ^ xor
		
		bucket0 = 0
		bucket1 = 0
		
		for i in nums:
		    
		    if first_set_bit & i == 0:
		        bucket0 ^= i
		    else:
		        bucket1 ^= i
		        
		if bucket0 > bucket1:
		    return [bucket1, bucket0]
		    
		return [bucket0, bucket1]
		
		



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		v = list(map(int,input().split()))
		ob = Solution();
		ans = ob.singleNumber(v)
		for i in ans:
			print(i, end = " ")
		print()

# } Driver Code Ends