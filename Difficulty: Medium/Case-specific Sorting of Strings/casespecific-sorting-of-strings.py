class Solution:
    def caseSort(self,s):
        #code here
        
        upper_case = []
        
        lower_case = []
        
        n = len(s)
        
        for i in range(n):
            
            if ord(s[i]) >= 97:
                lower_case.append(s[i])
            else:
                upper_case.append(s[i])
                
        
        # if len(upper_case ) == 0:
            
        #     return
                
                
        # apply the merge sort algo
        
        # self.merge_sort(upper_case, 0, len(upper_case) - 1)
        # self.merge_sort(lower_case, 0, len(lower_case) - 1)
        
        upper_case.sort()
        lower_case.sort()
        
        res_str = ""
        upper = 0
        lower = 0
        
        for i in range(len(s)):
            
            if ord(s[i]) >= 97:
                res_str += lower_case[lower]
                lower += 1
            else :
                res_str += upper_case[upper]
                upper += 1
                
        return res_str
        
        
        
    # def merge_sort(self, nums, low, high):
        
    #     if (low >= high):
    #         return
        
    #     mid = low + (high - low) // 2
        
    #     self.merge_sort(nums, low, mid)
    #     self.merge_sort(nums, mid + 1, high)
    #     self.merge(nums, low, mid, high)
        
    # def merge(self, nums, low, mid, high):
        
    #     left = low
    #     right = mid + 1
        
    #     lis = []
        
    #     while (left <= mid and right <= high):
            
    #         if (ord(nums[left]) <= ord(nums[right])):
    #             lis.append(nums[left])
    #             left += 1
    #         else:
    #             lis.append(nums[right])
    #             right += 1
                
    #     while (left <= mid):
            
    #         lis.append(nums[left])
    #         left += 1
            
    #     while (right <= high):
            
    #         lis.append(nums[right])
    #         right += 1
            
    #     for i in range(len(lis)):
            
    #         nums[low] = lis[i]
    #         low += 1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        