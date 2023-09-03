#User function Template for python3


class Solution:
    
    #Function is to check whether two strings are anagram of each other or not.
    def isAnagram(self,a,b):
        #code here
        n1 = len(a)
        n2 = len(b)
        if(n1 != n2):
            return False
        a = sorted(a)
        b = sorted(b)
        
        for i in range(n1):
            if(a[i] != b[i]):
                return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        a,b=map(str,input().strip().split())
        if(Solution().isAnagram(a,b)):
            print("YES")
        else:
            print("NO") 
# } Driver Code Ends