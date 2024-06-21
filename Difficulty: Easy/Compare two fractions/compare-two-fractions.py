#User function Template for python3


class Solution:
    def compareFrac (self, str):
        
        # code here
        
        lis = str.split(",")
        
        if lis[0] == lis[1]:
            return "equal"
            
        fir = lis[0].split("/")
        lst = lis[1].split("/")
        
        res_fir = int(fir[0]) / int(fir[1])
        res_lst = int(lst[0]) / int(lst[1])
        
        if res_fir == res_lst:
            return "equal"
        
        if res_fir > res_lst:
            return lis[0].strip()
            
        return lis[1].strip()



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends