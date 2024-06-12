
class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        cnt = 0
        
        for i in range(1, n + 1):
            
            if self.checkFourDigit(i):
                cnt += 1
                
        return cnt
        
    def checkFourDigit(self, digit):
        
        while (digit > 0):
            
            if (digit % 10 == 4):
                return True
                
            digit //=10
                
        return False
                
    
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.countNumberswith4(n)

        print(res)

# } Driver Code Ends