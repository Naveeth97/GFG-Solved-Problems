#User function Template for python3

class Solution:
    def solve(self,n,k,stalls):
        
        stalls.sort()
        
        low = 1
        high = stalls[len(stalls) - 1]
        mid = 0
        
        while(low <= high):
            mid = (low + high)//2
            
            if(self.canWePlace(stalls, mid, k) == True):
                
                low = mid + 1
            else:
                high = mid - 1
    
        return high
        
    
    def canWePlace(self, stalls,distance,cows):
        
        last = stalls[0]
        cowsCount = 1
        
        for i in range(1, len(stalls)):
            
            if((stalls[i] - last) >= distance):
                last  = stalls[i]
                cowsCount += 1
            
        if(cowsCount >= cows):
            return True
                
        return False
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = list(map(int, input().split()))
        stalls = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(n, k, stalls)
        print(res)

        T -= 1


if __name__ == "__main__":
    main()
# } Driver Code Ends