class Solution:
    def sameFreq(self, s: str) -> bool:
        #code here
        
        str_dic = {}
        
        for i in s:
            
            if i not in str_dic:
                
                str_dic[i] = 1
            else:
                
                str_dic[i] += 1
                
        
        res_dic = {}
        
        for i in str_dic:
            
            if str_dic[i] not in res_dic:
                
                res_dic[str_dic[i]] = 1
            else:
                
                res_dic[str_dic[i]] += 1
                
        
        
        if len(res_dic) == 1:
            return True
            
        
        if len(res_dic) == 2:
            
            lis = list(res_dic.keys())
            
            key1 = lis[0]
            key2 = lis[1]
            
            if res_dic[key1] == 1 and key1 == 1:
                
                return True
                
            if res_dic[key2] == 1 and key2 == 1:
                
                return True
                
            if abs(key1 - key2) == 1:
                
                if key1 > key2 and res_dic[key1] == 1 or key2 > key1 and res_dic[key2] == 1:
                    
                    return True
            
        return False