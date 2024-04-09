class Solution:
    def alternateSort(self,arr, N):
        # Your code goes here
        
        lis = [] * N
        
        arr.sort()
        
        i = 0
        j = N - 1
        while(i < j):
            
            lis.append(arr[j])
            lis.append(arr[i])
            # print(lis)
            j-=1
            i+=1
            
        while(i <= j):
            lis.append(arr[i])
            i+=1
            
        return lis


#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    def printAns(ans):
        for x in ans:
            print(x, end=" ");
        print()
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        obj=Solution()
        ans=obj.alternateSort(a,n)
        printAns(ans)
# } Driver Code Ends