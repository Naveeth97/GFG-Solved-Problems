#User function Template for python3

class Solution:
    def reverseWords(self, s):
        # code here
        
        res = []
        next_str = ''
        
        for i in range(len(s) - 1, -1, -1):
            
            if s[i] == '.':
                res.insert(0, next_str)
                next_str=''
            
            else:
                next_str += s[i]
                
        res.insert(0,next_str)
                
                
        return '.'.join(res)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseWords(s)
        print(ans)
# } Driver Code Ends