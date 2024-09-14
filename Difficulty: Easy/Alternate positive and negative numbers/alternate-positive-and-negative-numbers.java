//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String input = br.readLine();
            String[] inputArray = input.split("\\s+");
            ArrayList<Integer> arr = new ArrayList<>();

            for (String s : inputArray) {
                arr.add(Integer.parseInt(s));
            }

            new Solution().rearrange(arr);
            for (int num : arr) {
                System.out.print(num + " ");
            }
            System.out.println();
        }
    }
}

// } Driver Code Ends


// User function Template for Java
class Solution {
    void rearrange(ArrayList<Integer> arr) {
        Queue<Integer> arr1 = new LinkedList<>();
        Queue<Integer> arr2 = new LinkedList<>();
        for(int i : arr) {
            if(i >= 0) arr1.add(i);
            else arr2.add(i);
        }
        int i = 0;
        while(!arr1.isEmpty() || !arr2.isEmpty()) {
            if(!arr1.isEmpty()) {
                arr.set(i , arr1.poll());
                i++;
            }
            if(!arr2.isEmpty()) {
                arr.set(i , arr2.poll());
                i++;
            }
        }
        
    }
}

