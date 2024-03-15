#User function Template for python3

class Solution:
    #def missing(self,arr,n,lis):
        
        
    def findTwoElement( self,arr, n): 
        
        sn = (n*(n+1))//2
        s2n = (n*(n+1)*(2*n+1))//6
        s1,s2 = 0, 0
        repeating = -1
        missing = -1
        
        for i in range(n):
            s1 += arr[i]
            s2 += (arr[i] * arr[i])
            
        val1 = sn - s1
        val2 = s2n - s2
        
        val2 = val2//val1
        
        missing = (val1 + val2)//2
        repeating = missing - val1
        
        return [repeating,missing]
        
        
        
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends