#User function Template for python3
class Solution:

	def valueEqualToIndex(self,arr, n):
		# code here
		
		lis = []
		
		for i in range(1,n+1):
		    
		    if i == arr[i - 1]:
		        lis.append(i)
		        
		return lis


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.valueEqualToIndex(arr, n)
        if len(ans) == 0:
            print("Not Found")
        else:
            for x in ans:
                print(x, end=" ")
            print()
        tc -= 1

# } Driver Code Ends