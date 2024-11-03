class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        
        return self.mergeSort(arr, 0, len(arr) - 1)
        
    def mergeSort(self, arr, low, high):
        
        cnt = 0
        
        if low >= high:
            return cnt
        
        mid = (low + high) >> 1
        cnt += self.mergeSort(arr, low, mid)
        cnt += self.mergeSort(arr, mid + 1, high)
        cnt += self.merge(arr, low, mid, high)
        
        return cnt
        
    def merge(self, arr, low, mid, high):
        
        left = low
        right = mid + 1
        cnt = 0
        
        lis = []
        
        while left <= mid and right <= high:
            
            if arr[left] <= arr[right]:
                lis.append(arr[left])
                left += 1
            else:
                lis.append(arr[right])
                cnt += (mid - left + 1)
                right += 1
        
        while left <= mid:
            
            lis.append(arr[left])
            left += 1
            
        while right <= high:
            
            lis.append(arr[right])
            right += 1
            
        for i in range(low, high + 1):
            
            arr[i] = lis[i - low]
            
        return cnt
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends