# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        arr = S.split('.')
        i = len(arr) - 1
        res = list()
        while(i>=0):
            res.append(arr[i])
            i-=1
        res = '.'.join(res)
        return res
            
            


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends