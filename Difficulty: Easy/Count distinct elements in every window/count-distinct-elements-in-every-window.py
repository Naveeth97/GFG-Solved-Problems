
class Solution:
    def countDistinct(self, arr, k):
        # Code here
        
        distinct_count = []
        
        hash_map = {}
        
        left, right = 0, 0
        
        while right < k:
            
            if arr[right] not in hash_map:
                
                hash_map[arr[right]] = 0
            
            hash_map[arr[right]] += 1
            right += 1
            
        distinct_count.append(len(hash_map))
            
        while right < len(arr):
            
            hash_map[arr[left]] -= 1
            
            if hash_map[arr[left]] == 0:
                hash_map.pop(arr[left])
                
            left += 1
            
            if arr[right] not in hash_map:
                
                hash_map[arr[right]] = 0
                
            hash_map[arr[right]] += 1
            distinct_count.append(len(hash_map))
            
            right += 1
            
        return distinct_count
                
            
            
            
            
            


#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends