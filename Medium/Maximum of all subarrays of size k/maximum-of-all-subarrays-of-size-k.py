#User function Template for python3
from collections import deque
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        #code here
        di = deque()
        lis = []
        for i in range(k):
            
            while di and arr[i]>=arr[di[-1]]:
                di.pop()
                
            di.append(i)
            
        for i in range(k,n):
            
            lis.append(arr[di[0]])
            
            while di and di[0]<=i-k:
                di.popleft()
                
            while di and arr[i]>=arr[di[-1]]:
                di.pop()
                
            di.append(i)
            
        lis.append(arr[di[0]])
        return lis
            
            
            
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends