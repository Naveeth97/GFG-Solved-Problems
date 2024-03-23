#User function Template for python3

class Solution:
    def firstRep(self, s):
        # code here
        maps = {}
        
        for i in s:
            
            if(i in maps):
                maps[i] += 1
            else:
                maps[i] = 1
                
        for i in s:
            if maps[i] > 1:
                return i
                
        return '#'


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.firstRep(s)
        if ans is '#':
            print(-1)
        else:
            print(ans)
        
# } Driver Code Ends