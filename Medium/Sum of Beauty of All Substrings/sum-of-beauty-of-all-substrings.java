//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0){
            //br.readLine();
            String s;
            s = br.readLine();
            
            Solution obj = new Solution();
            int res = obj.beautySum(s);
            
            System.out.println(res);
            
        }
    }
}

// } Driver Code Ends


class Solution {
    public static int beautySum(String s) {
        // code here
        
        int beauty = 0, maxi = 0, min  = 1000;
        
        for(int i = 0;i<s.length();i++){
            int[] count = new int[26];
            
            for(int j = i;j<s.length();j++){
                
                ++count[s.charAt(j) - 'a'];
                maxi = 0;
                min = 1000;
                
                for(int freq : count){
                    if(freq > 0){
                        maxi = Math.max(maxi, freq);
                        min = Math.min(min, freq);
                    }
                }
                
                beauty += (maxi - min);
            }
            
        }
        
        
        return beauty;
    }
}
        
