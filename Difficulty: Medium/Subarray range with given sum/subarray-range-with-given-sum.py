#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    
    #Complete this fuction
    #Function to count the number of subarrays which adds to the given sum.
    def subArraySum(self,arr, tar):
        #Your code here
        
        subarray_count = 0
        
        maps = {}
        sum = 0
        
        for i in range(len(arr)):
            
            sum += arr[i]
            
            if sum == tar:
                subarray_count += 1
                
            if (sum - tar) in maps:
                
                subarray_count += 1
            
            if sum not in maps:
                
                maps[sum] = 1;
                
        if sum - tar in maps:
            subarray_count += 1
                
        return subarray_count
                
                

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        tar= int(input())
        ob = Solution()
        res = ob.subArraySum(arr,tar)
        print(res)
        # print("~")
        t -= 1


# } Driver Code Ends