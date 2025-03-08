class Solution:
    def celebrity(self, mat):
        # code here
        
        for i in range(len(mat)):
            
            cnt = 0
            
            for j in range(len(mat[i])):
                
                if i == j:
                    continue
                
                if mat[j][i] == 1 and mat[i][j] == 0:
                    cnt += 1
                    
            if cnt == len(mat) - 1:
                return i
                    
        return -1


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
        print("~")

# } Driver Code Ends