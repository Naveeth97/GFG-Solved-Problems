class Solution {
    public ArrayList<Integer> findGreater(int[] arr) {
        // code here
        
        ArrayList<Integer> ans = new ArrayList<>();
        
        int fq [] = new int[100000+1];
        
        for(int i=0;i<arr.length;i++)
        {
            fq[arr[i]]++;
        }
        
        for(int i=0;i<arr.length;i++)
        {
            int j=i+1;
            
            while(j<arr.length && fq[arr[i]] >= fq[arr[j]] )
            {
                j++;
            }
            
            if(j==arr.length) ans.add(-1);
            else
            ans.add(arr[j]);
            
        }
        
        return ans;
        
    }
}