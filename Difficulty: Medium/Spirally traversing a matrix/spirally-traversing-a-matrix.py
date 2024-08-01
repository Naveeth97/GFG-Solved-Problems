class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix):
        # code here
        
        spiral = []
        
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1
        
        while (left <= right and top <= bottom):
            
            for i in range(left, right + 1):
                spiral.append(matrix[top][i])
            top += 1
                
            for i in range(top, bottom + 1):
                spiral.append(matrix[i][right])
                
            right -= 1
            
            if (top <= bottom):
                
                for i in range(right, left - 1, -1):
                    spiral.append(matrix[bottom][i])
                    
                bottom -= 1
                
            if (left <= right):
                
                for i in range(bottom, top - 1, -1):
                    spiral.append(matrix[i][left])
                    
                left += 1
                
        return spiral
        
        # spiral = []

        # left, right = 0, len(matrix[0]) - 1
        # top, bottom = 0, len(matrix) - 1

        # while(left <= right and top <= bottom):

        #     for i in range(left, right + 1):
        #         spiral.append(matrix[top][i])
            
        #     top += 1

        #     for i in range(top, bottom + 1):
        #         spiral.append(matrix[i][right])
            
        #     right -= 1

        #     if(top <= bottom):

        #         for i in range(right, left - 1, -1):
        #             spiral.append(matrix[bottom][i])
                
        #         bottom -= 1
            
        #     if(left <= right):

        #         for i in range(bottom, top - 1, -1):
        #             spiral.append(matrix[i][left])

        #         left += 1
        
        # return spiral


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))

# } Driver Code Ends