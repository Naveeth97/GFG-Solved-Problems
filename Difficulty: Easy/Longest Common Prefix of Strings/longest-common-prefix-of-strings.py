#User function Template for python3

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        
        arr.sort()
        
        temp = arr[0]
        
        res = arr[-1]
        
        prefix = ""
        
        for i in range(len(temp)):
            
            if (temp[i] != res[i]):
                break
            prefix += temp[i]
                
            
        if (len(prefix) == 0):
            return -1
            
        return prefix
                
                
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends