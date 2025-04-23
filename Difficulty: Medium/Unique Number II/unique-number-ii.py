#User function Template for python3

class Solution:
	def singleNum(self, nums):
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
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.singleNum(arr)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends