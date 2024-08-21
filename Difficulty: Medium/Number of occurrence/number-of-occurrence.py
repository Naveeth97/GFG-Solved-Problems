#User function Template for python3
class Solution:

    def count(self,arr, n, x):
        # code here
        if(n == 1):
            if(arr[0] == x):
                return 1
        if(n == 2):
            if(arr[0] == x and arr[1] == x):
                return 2
            elif(arr[0] == x and arr[1] != x):
                return 1
            elif(arr[1] == x and arr[0] != x):
                return 1
        i = self.firstoccur(arr,n,x)
        j = self.lastoccur(arr,n,x)
        
        if(i == -1):
            return 0
            
        return j - i + 1
        
        
            
        
           
        
    def firstoccur(self,arr,n,x):
        start, end = 0,n-1
        while(start<=end):
            mid = (start + end)//2
            if(arr[mid]>x):
                end = mid - 1
            elif(arr[mid]<x):
                start = mid + 1
            else:
                if(mid == 0 or arr[mid] == x and arr[mid-1] != x):
                    return mid
                else:
                    end = mid - 1
        return -1
    def lastoccur(self,arr,n,x):
        start, end = 0,n-1
        while(start<=end):
            mid = (start + end)//2
            if(arr[mid]>x):
                end = mid - 1
            elif(arr[mid]<x):
                start = mid + 1
            else:
                if(mid == n - 1 or arr[mid] == x and arr[mid + 1] != x):
                    return mid
                else:
                    start = mid + 1
        return -1
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends