#{ 
 # Driver Code Starts


#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def removeOuter(self, S):
        # Code here
        count = 0
        resString = "";
        
        for i in range(len(S)):
            
            if(S[i] == '('):
                
                if(count > 0):
                    resString += S[i]
                    
                count += 1
                    
            else:
                
                count -= 1
                
                if(count > 0):
                    resString += S[i]
                    
                
            
        return resString
                
                    

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        s = input()
        ob = Solution()
        res = ob.removeOuter(s)
        print(res)
# } Driver Code Ends