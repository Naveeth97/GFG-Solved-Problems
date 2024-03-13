# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        # code here
        lis = []
        i = 0
        j = 0
        
        row = len(mat[0])
        column = len(mat)
        up_dir = True
        
        while(i < row and j < column):
            
            if up_dir:
                
                while(i >0 and j < column - 1):
                    
                    lis.append(mat[i][j])
                    i -= 1
                    j  += 1
                    
                lis.append(mat[i][j])
                    
                if (j == column - 1):
                    i += 1
                else:
                    j += 1
            else:
                
                while(i < row - 1 and j > 0):
                    
                    lis.append(mat[i][j])
                    j -= 1
                    i += 1
                
                lis.append(mat[i][j])
                
                if(i == row - 1):
                    j += 1
                else:
                    i += 1
                    
            if(up_dir):
                up_dir = False
            else:
                up_dir = True
                
        return lis
                


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends