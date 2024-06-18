#User function template for Python

class Solution:
    def rectanglesInCircle(self,r):
        #code here
        rectangle = 0
        
        for l in range(1, (2 * r) + 1):
            
            for b in range(1, (2*r) + 1):
                
                if l*l + b*b <= 4*r * r:
                    rectangle += 1
                    
        return rectangle
                


#{ 
 # Driver Code Starts
#Initial Template for Python

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.rectanglesInCircle(N)
        print(ans)

# } Driver Code Ends