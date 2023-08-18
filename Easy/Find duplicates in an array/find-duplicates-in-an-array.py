from collections import Counter
class Solution:

    def duplicates(self, arr, n): 
    	# code here
    	res = []
    	coun = Counter(arr)
    	for i in coun.keys():
    	    if(coun[i]>1):
    	        res.append(i)
    	if(len(res)>=1):
    	    res.sort()
    	    return res
    	else:
    	    res.append(-1)
    	    return res
    	
    	
    	        
    	    


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends