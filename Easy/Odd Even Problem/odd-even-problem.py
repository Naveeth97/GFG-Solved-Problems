
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        
        even = 0
        odd = 0
        
        temp = ""
        
        for i in s:
            
            if i not in temp:
                temp += i
                
        # print(temp)
        
        alpha = "bdfhjlnprtvxz"
        
        for i in temp:
            
            if i in alpha:
                
                if s.count(i) % 2 == 0:
                    even += 1
                
            else:
                
                if s.count(i) % 2 == 1:
                    odd += 1
                    
                
                    
        if (odd + even) % 2 == 0:
            return "EVEN"
        return "ODD"
        
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends