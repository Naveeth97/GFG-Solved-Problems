#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        low,high = 0,n-1
        min_index = 0
        min_element = arr[0]
        while(low<=high):
            mid = (low + high)//2
            if(arr[low]<=arr[mid]):
                if(arr[low]<=min_element):
                    min_element = arr[low]
                    min_index = low
                low = mid + 1
            else:
                if(arr[mid]<=min_element):
                    min_element = arr[mid]
                    min_index = mid
                high = mid - 1
        return min_index
                
                
                    
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends