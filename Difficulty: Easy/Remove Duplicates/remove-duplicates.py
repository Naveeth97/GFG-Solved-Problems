#User function Template for python3
class Solution:
	def removeDups(self, str):
		# code here
		
		res = ""
		
		for i in range(len(str)):
		    
		    if str[i] not in res:
		        
		        res += str[i]
		        
	    return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends