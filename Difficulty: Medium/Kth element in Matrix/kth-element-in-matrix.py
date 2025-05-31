class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]
        
        while left < right:
            mid = (left + right) // 2
            count = self.countLessEqual(matrix, mid)
            if count < k:
                left = mid + 1
            else:
                right = mid
        return left

    def countLessEqual(self, matrix, mid):
        n = len(matrix)
        count = 0
        for row in matrix:
            # Binary search in each row
            l, r = 0, n
            while l < r:
                m = (l + r) // 2
                if row[m] <= mid:
                    l = m + 1
                else:
                    r = m
            count += l
        return count
                    
            
                    
        
        
        
        
        