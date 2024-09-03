#User function Template for python3

class Solution:
	def AllPossibleStrings(self, s):
		# Code here
        subset = 1 << len(s)
        
        lis = []
        
        for i in range(0, subset):
            
            str = ""
            
            for j in range(0, len(s)):
                
                if ((i & (1 << j)) > 0):
                    str += s[j]
                    
            if (len(str) > 0):
                lis.append(str)
                
        lis.sort()
        
        return lis

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends