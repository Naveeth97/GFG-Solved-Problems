#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
    	j = -1
    	for i in range(n):
    	    if(arr[i] == 0):
    	        j = i
    	        break
    	if(j==-1):
    	    return arr
    	for k in range(j+1,n):
    	    if(arr[k] != 0):
    	        arr[k],arr[j] = arr[j],arr[k]
    	        j+=1
    	return arr
    	    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends