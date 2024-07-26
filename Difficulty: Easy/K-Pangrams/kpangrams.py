#User function Template for python3
class Solution:
    def kPangram(self,string, k):
    # code here
    
        if (len(string) < 26):
            return False
            
        lis = [0] * 26
        count = 0
        
        for i in range(len(string)):
            
            if (string[i] == ' '):
                continue

            lis[ord(string[i]) - 97] += 1
            
            count += 1
            
        if (count < 26):
            
            return False
            
        for i in range(26):
            
            if (lis[i] == 0):
                k -= 1
                
        if (k < 0):
            
            return False
            
        return True
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends