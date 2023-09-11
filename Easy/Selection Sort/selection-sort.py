#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        for j in range(len(arr)):
            min_idx = j
            for k in range(j+1,len(arr)):
                if(arr[min_idx]>arr[j]):
                    min_idx = k
        return arr[min_idx]
        
        
    
    def selectionSort(self, arr,n):
        #code here
        for x in range(len(arr)):
            min_idx1 = x
            for y in range(x+1,n):
                if(arr[min_idx1]>arr[y]):
                    min_idx1 = y
            arr[x],arr[min_idx1] = arr[min_idx1],arr[x]
        return arr
        
    
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends