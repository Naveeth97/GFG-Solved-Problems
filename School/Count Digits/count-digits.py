#User function Template for python3

class Solution:
    def evenlyDivides (self, N):
        # code here
        count = 0
        temp = N
        while(temp>0):
            dig = temp%10
            if(dig == 0):
                temp//=10
                continue
            if(N%dig == 0):
                count+=1
            temp//=10
                
        return count
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends