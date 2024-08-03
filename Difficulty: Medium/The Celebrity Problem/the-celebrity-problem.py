class Solution:
    def celebrity(self, mat):
        # code here
        celebrity = -1
        
        for i in range(len(mat)):
            
            count = 0
            
            for j in range(len(mat[0])):
                
                if i == j:
                    continue
                
                if (mat[i][j] == 1):
                    break
                
                if mat[i][j] == 0 and mat[j][i] == 1:
                    count += 1
                    
            if count == len(mat[0]) - 1:
                celebrity = i
                
        return celebrity

#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends