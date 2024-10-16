class Solution:
    def checkSorted(self, arr):
        #code here
        
        swaps = 0
        
        for i in range(len(arr)):
            
            if arr[i] != i + 1:
                
                self.swap(arr[i] - 1, i, arr)
                swaps += 1
                
        for i in range(len(arr) - 1):
            
            if arr[i] > arr[i + 1]:
                return False
                
        return swaps == 2 or swaps == 0
        
    def swap(self, fir, lst, arr):
        
        arr[fir] ^= arr[lst]
        arr[lst] ^= arr[fir]
        arr[fir] ^= arr[lst]


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        arr = list(map(int, input().split()))

        sol = Solution()
        result = sol.checkSorted(arr)
        if result:
            print("true")
        else:
            print("false")

# } Driver Code Ends