#User function Template for python3
class Solution:
    def isValid(self, str):
        #code here
        ip = str.split(".")
        
        if len(ip) != 4:
            return False
            
        for i in ip:
            
            # print(len(i))
            
            if (len(i) > 1 and i[0] == "0"):
                return False
                
            if (i == ""):
                return False
            
            ip_num = int(i)
            
            if ip_num < 0 or ip_num > 255:
                
                # print(ip_num)
                
                return False
                
        return True
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends