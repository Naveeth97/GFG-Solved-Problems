#User function Template for python3
import math


class Solution:
    def check_prime(self,sum):
        
        if(sum<=1):
            return False
            
        if(sum == 2 or sum == 3 or sum == 5):
            return True
        
        for i in range(2,int(math.sqrt(sum)) + 1):
            if(sum % i == 0):
                return False
        return True
                
        
    def minNumber(self, arr,n):
        # code here
        #min_prime = 0
        sum = 0
        for i in range(0,n):
            sum += arr[i]
    
        count = 0
        while(count<count+1):
            min_prime = self.check_prime(sum + count)
            if(min_prime):
                return count
            count += 1
            
        
            
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends