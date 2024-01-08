#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		largest = 0
		seclargest = 0
		
		for i in range(0,n):
		    if(arr[i]>largest):
		        seclargest = largest
		        largest = arr[i]
		        
		    elif(arr[i]>seclargest and arr[i] != largest):
		        seclargest = arr[i]
		        
		if(seclargest == 0):
		    return -1
		        
	    return seclargest


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends