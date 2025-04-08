class Solution:
    
    def inversionCount(self, arr):
        self.inversion_count = 0
        self.mergeSort(arr, 0, len(arr) - 1)
        return self.inversion_count

    def mergeSort(self, arr, start, end):
        if start == end:
            return
        mid = (start + end) // 2
        self.mergeSort(arr, start, mid)
        self.mergeSort(arr, mid + 1, end)
        self.merge(arr, start, mid, end)

    def merge(self, arr, start, mid, end):
        i = start
        j = mid + 1
        sorted_lis = []

        while i <= mid and j <= end:
            if arr[i] <= arr[j]:
                sorted_lis.append(arr[i])
                i += 1
            else:
                self.inversion_count += (mid - i + 1)
                sorted_lis.append(arr[j])
                j += 1

        while i <= mid:
            sorted_lis.append(arr[i])
            i += 1
        while j <= end:
            sorted_lis.append(arr[j])
            j += 1

        for idx in range(len(sorted_lis)):
            arr[start + idx] = sorted_lis[idx]

                


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