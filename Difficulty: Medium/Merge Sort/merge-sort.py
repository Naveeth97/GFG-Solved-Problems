#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
 
    def mergeSort(self,arr, l, r):
        #code here
        if (l != r):
            
            mid = (l + r) // 2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            self.merge(arr, l, mid, r)
        
    def merge(self, arr, start, mid, end):
        
        i = start
        j = mid + 1
        
        sorted_lis = []
        
        while i <= mid and j <= end:
            
            if arr[i] <= arr[j]:
                sorted_lis.append(arr[i])
                i += 1
            else:
                sorted_lis.append(arr[j])
                j += 1
                
        while i <= mid:
            
            sorted_lis.append(arr[i])
            i += 1
            
        while j <= end:
            
            sorted_lis.append(arr[j])
            j += 1
            
        sorted_idx = 0
            
        for index in range(start, end + 1):
            
            arr[index] = sorted_lis[sorted_idx]
            sorted_idx += 1
            
        



#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.mergeSort(arr,0,len(arr)-1)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends