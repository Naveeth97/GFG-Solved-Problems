#User function Template for python3

class Solution:
    def findMin(self, arr, n):
        #complete the function here
        if(n == 0):
            return None
        min = arr[0]
        start,end = 0,n-1
        while(start<=end):
            mid = (start + end)//2
            if(arr[start]<=arr[mid]):
                if(arr[start]<=min):
                    min = arr[start]
                start = mid + 1
                
            else:
                if(arr[mid]<=min):
                    min = arr[mid]
                end = mid - 1
        return min
                        
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.findMin(arr, n))
# } Driver Code Ends