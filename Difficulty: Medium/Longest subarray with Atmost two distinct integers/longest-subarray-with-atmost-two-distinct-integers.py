class Solution:
    def totalElements(self, arr):
        # Code here
        
        # sliding window strategy
        
        mpp = {}
        
        left = 0
        right = 0
        
        n = len(arr)
        res = 0
        
        
        while right < n:
            
            if arr[right] not in mpp:
                
                mpp[arr[right]] = 0
                
            mpp[arr[right]] += 1
            
            if len(mpp) > 2:
                
                mpp[arr[left]] -= 1
                
                if mpp[arr[left]] == 0:
                    
                    del mpp[arr[left]]
                    
                left += 1
                
            res = max(res, right - left + 1)
            right += 1
            
        return res
                
                
                
            
            
            