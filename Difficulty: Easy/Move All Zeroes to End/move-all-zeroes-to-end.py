#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	
    	fir = 0
    	sec = 0
    	
    	while fir < len(arr):
    	    
    	    if arr[sec] != 0:
    	        sec += 1
    	        
    	    elif arr[sec] == 0 and arr[fir] != 0:
    	        
    	        arr[sec] ^= arr[fir]
    	        arr[fir] ^= arr[sec]
    	        arr[sec] ^= arr[fir]
    	        sec += 1
    	        
    	    fir += 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends