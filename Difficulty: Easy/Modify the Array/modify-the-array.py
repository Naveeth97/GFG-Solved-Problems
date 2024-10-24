#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        
        for i in range(len(arr) - 1):
            
            if arr[i] == arr[i + 1]:
                
                arr[i] *= 2
                arr[i + 1]  = 0
                
        fir, lst = 0, 1
        
        while (lst < len(arr)):
            
            if arr[fir] == 0 and arr[lst] == 0:
                lst += 1
                continue
            
            if arr[fir] == 0:
                self.swap(arr, fir, lst)
            fir += 1
            lst += 1
            
        return arr
            
    def swap(self, arr, fir, lst):
        
        arr[fir] ^= arr[lst]
        arr[lst] ^= arr[fir]
        arr[fir] ^= arr[lst]
                
                
                


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.modifyAndRearrangeArr(arr)
        print(*ans)
        print("~")
        t -= 1


# } Driver Code Ends