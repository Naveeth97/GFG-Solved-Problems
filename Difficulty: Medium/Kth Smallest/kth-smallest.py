#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        
        #according to given complexity
        
        max_element = 0
        
        for i in arr:
            
            max_element = max(max_element, i)
            
            
        freq = [0] * (max_element + 1)
        
        for i in arr:
            
            freq[i] += 1
            
        for i in range(len(freq)):
            
            if freq[i] > 0:
                k -= 1
                
            if k == 0:
                
                return i
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))

# } Driver Code Ends