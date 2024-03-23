#User function Template for python3
class Solution:
    def sameFreq(self, s):
        # code here
        lis = [0] * 26
        
        for i in range(len(s)):
            
            lis[ord(s[i]) - 97] += 1
            
        if(self.allsame(lis)):
            return True
            
        for k in range(26):
            
            if(lis[k] > 0):
                lis[k] -= 1
                
                if(self.allsame(lis)):
                    return True
                
                lis[k] += 1
        
        return False
            
        
        
    def allsame(self, lis):
        
        same = 0
        
        for i in lis:
            if(i > 0):
                same = i
                break
        
        for j in range(len(lis)):
            
            if(lis[j] > 0 and lis[j] != same):
                return False
        
        return True
        
        
        
            
            
            
        
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends