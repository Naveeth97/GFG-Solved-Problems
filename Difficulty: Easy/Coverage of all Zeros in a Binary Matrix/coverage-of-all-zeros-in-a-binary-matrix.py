#User function Template for python3

class Solution:
	def findCoverage(self, matrix):
		# Code here
		
		count = 0
		n = len(matrix)
		m = len(matrix[0])
		
		for i in range(len(matrix)):
		    
		    for j in range(len(matrix[0])):
		        
		        if matrix[i][j] == 0:
		            
		            #checks upwards
		            if i > 0 and matrix[i - 1][j] == 1:
		                count += 1
		            
		            #checks downwards
		            
		            if i < n - 1 and matrix[i + 1][j] == 1:
		                count += 1
		            
		            #checks left
		            if j > 0 and matrix[i][j - 1] == 1:
		                count += 1
		            
		            
		            #checks right
		            if j < m - 1 and matrix[i][j + 1] == 1:
		                count += 1
	    
	    return count


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.findCoverage(matrix)
        print(ans)

# } Driver Code Ends