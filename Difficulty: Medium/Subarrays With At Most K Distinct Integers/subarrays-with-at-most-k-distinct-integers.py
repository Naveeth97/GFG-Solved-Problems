class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        
        count = 0
        
        n = len(arr)
        
        left = 0
        right = 0
        
        dic = {}
        
        while right < n:
            
            if arr[right] not in dic:
                
                dic[arr[right]] = 0
                
            dic[arr[right]] += 1
            
            while len(dic) > k:
                
                dic[arr[left]] -= 1
                
                if dic[arr[left]] == 0:
                    
                    del dic[arr[left]]
                    
                left += 1
                
            count += right - left + 1
            
            right += 1
            
        return count
                    
                    
            
            