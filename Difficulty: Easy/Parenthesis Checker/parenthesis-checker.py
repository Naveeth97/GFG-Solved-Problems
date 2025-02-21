
class Solution:
    def isBalanced(self, s):
        # code here
        
        mpp = {'}' : '{', ']':'[', ')':'('}
        
        lis = []
        
        for i in range(len(s)):
            
            if s[i] == '{' or s[i] == '(' or s[i] == '[':
                lis.append(s[i])
                continue
                
            ch = s[i]
            
            # print(lis)
            
            if ch == ']' or ch == ')' or ch == '}':
                
                if len(lis) == 0 or mpp[ch] != lis[-1]:
                    return False
                
                lis.pop()
                
                
        return len(lis) == 0
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

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
    for cases in range(test_cases):
        s = str(input())
        obj = Solution()
        if obj.isBalanced(s):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends