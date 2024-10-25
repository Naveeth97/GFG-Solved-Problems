class Solution:
    def alternateSort(self,arr):
        # Your code goes here
        
        arr.sort()
        
        lis = [0] * len(arr)
        
        i, j = 0, len(arr) - 1
        
        for k in range(len(arr)):
            
            if k % 2 == 0:
                lis[k] = arr[j]
                j -= 1
            else:
                lis[k] = arr[i]
                i += 1
                
        return lis
        
        
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.alternateSort(arr)
        print(*ans)
        print("~")
        t -= 1

# } Driver Code Ends