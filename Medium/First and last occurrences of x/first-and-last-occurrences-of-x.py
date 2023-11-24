#User function Template for python3


class Solution:
    def firstoccurence(self,arr,n,x):
        
        low,high = 0,n -1
        
        while(low<=high):
            mid = (low + high)//2
            
            if(arr[mid] == x and (mid == 0 or arr[mid - 1] != x)):
                return mid
                
            elif(mid == 0 or arr[mid - 1] == x):
                high = mid - 1
                
            else:
                if(arr[mid] < x):
                    low = mid + 1
                    
                else:
                    high = mid - 1
                    
        return -1
                
    def lastoccurence(self,arr,n,x):
        
        low,high = 0,n - 1
        
        while(low<=high):
            mid = (low + high)//2
            
            if(arr[mid] == x and (mid == n - 1 or arr[mid + 1] != x)):
                return mid
                
            elif(mid == n - 1 or arr[mid + 1] == x):
                low = mid + 1
                
            else:
                if(arr[mid] < x):
                    low = mid + 1
                    
                else:
                    high = mid - 1
                    
        return -1 
        
        
    def find(self, arr, n, x):
        
        # code here
        #edge case
        if(arr[0] == x and arr[n - 1] == x):
            return [0,n-1]
        
        lis = []
        first_index = self.firstoccurence(arr,n,x)
        last_index = self.lastoccurence(arr,n,x)
        
        lis.append(first_index)
        lis.append(last_index)
        
        return lis
        


#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends