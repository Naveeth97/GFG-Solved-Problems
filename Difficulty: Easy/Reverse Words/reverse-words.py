# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,str):
        # code here 
        res_str = ""
        temp = ""
        
        for i in range(len(str)):
            
            if str[i] == ".":
                res_str  = temp +"." + res_str
                temp = ""
            else:
                temp += str[i]
                
        # print(res_str, len(res_str))
                
        return temp+"."+res_str[:len(res_str) - 1]

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