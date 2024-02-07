# User function Template for python3

class Solution:
    
    def dot(self, lis):
        
        str =""
        
        for i in lis:
            
            str = str + i + "."
            
        return str[0:len(str) - 1]
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        
        lis = []
        temp = ""
        
        
        for i in range(len(S)):
            
            ch = S[i]
            
            if(ch == "."):
                
                if(temp != ""):
                    
                   lis.insert(0, temp)
                   
                temp = ""
                
            else:
                temp += ch
                
        if(len(temp) > 0):
            lis.insert(0, temp)
                
        return self.dot(lis)


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