#User function Template for python3

class Solution:
    def removeChars (ob, string1, string2):
        # code here 
        maps = {}
        
        for i in string2:
            
            if i in maps:
                maps[i] += 1
            else:
                maps[i] = 1
                
        res = ""
        
        for j in string1:
            
            if j not in maps:
                res += j
                
        return res
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        string1=input()
        string2=input()
        
        ob = Solution()
        print(ob.removeChars(string1,string2))
# } Driver Code Ends