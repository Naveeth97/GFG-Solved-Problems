#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        num, count = N, 0
        if(len(str(num)) == 1):
            return 1
        while(num != 0):
            r = num %10
            if r>0 and N%r==0:
                count +=1
            num//=10
    
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