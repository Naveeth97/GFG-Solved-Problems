#User function Template for python3

class Solution:
    def DivisibleByEight(self,s):
        #code here
        
        if(len(s) == 0):
            return 0
        if(len(s) < 3 and int(s) % 8 ==0):
            
            return 1
            
    
            
        hund = int(s[-3])
        tens = int(s[-2])
        ones = int(s[-1])
        
        
        if((hund * 100) + (tens * 10) + ones) % 8 == 0:
            return 1
        else:
            return -1
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.DivisibleByEight(S))
# } Driver Code Ends