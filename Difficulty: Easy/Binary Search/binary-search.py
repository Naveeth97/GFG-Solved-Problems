#User function template for Python

class Solution:    
    def binarysearch(self, arr, k):
        # code here
        
        n = len(arr)        
        low = 0
        high = n - 1
        mid = 0
        
        while(low<=high):
            mid = (low + high)//2
            
            if(arr[mid] == k):
                return mid
            elif(arr[mid]>k):
                high = mid - 1
            else:
                low = mid + 1
                
        return -1











#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.binarysearch(arr, k)
        print(res)

# } Driver Code Ends