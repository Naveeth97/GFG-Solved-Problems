#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
		# code here
		str = ""
		temp = ""
		
		for i in S:
		    
		    if(i == " " and len(temp) > 0):
		        
		        str += temp[0]
		        temp = ""
		        
		    else:
		        temp += i
		        
		if(len(temp) > 0):
		    str += temp[0]
		        
		return str
		        
		    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.firstAlphabet(S)
		
		print(answer)


# } Driver Code Ends