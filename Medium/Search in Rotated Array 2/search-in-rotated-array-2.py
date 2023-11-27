#User function Template for python3

class Solution:
    def Search(self, n, arr, k):
        # code here
        low,high = 0,n - 1
        while(low<=high):
            mid = (low + high)//2
            
            if(arr[mid] == k):
                return 1
                
            if((arr[low] == arr[mid]) and (arr[mid] == arr[high])):
                low += 1
                high -= 1
                continue
            
            if(arr[low]<=arr[mid]):
                if(k>=arr[low] and k<=arr[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
                    
            else:
                if(k>=arr[mid] and k<=arr[high]):
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return 0
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        ans = ob.Search(n, arr, k)
        print(ans)
        tc -= 1
# } Driver Code Ends