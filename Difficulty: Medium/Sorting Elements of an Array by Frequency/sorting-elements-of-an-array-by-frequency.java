//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.lang.*;
import java.util.*;
import java.util.Map.Entry;


// } Driver Code Ends
// User function Template for Java

class Solution {
    // Function to sort the array according to frequency of elements.
    public ArrayList<Integer> sortByFreq(int arr[]) {
        // add your code here
        ArrayList<Integer> ans = new ArrayList<>();
        Map<Integer, Integer> freqSort = new TreeMap<>();
        
        for (int i = 0; i < arr.length; i++) {
            
            if (freqSort.containsKey(arr[i])) {
                freqSort.put(arr[i], freqSort.get(arr[i]) + 1);
            } else {
                freqSort.put(arr[i], 1);
            }
        }
        
        List<Map.Entry<Integer, Integer>> list = new LinkedList<Map.Entry<Integer, Integer>>
        (freqSort.entrySet());
        
        Collections.sort(list, new Comparator<Map.Entry<Integer, Integer>>() {
            public int compare(Map.Entry<Integer, Integer> o1,
                            Map.Entry<Integer, Integer> o2) {
                                return (o2.getValue()).compareTo(o1.getValue());
                            }
        });
        
        for (Map.Entry<Integer, Integer> list1 : list) {
            
            for (int i = 0; i < list1.getValue(); i++) {
                ans.add(list1.getKey());
            }
        }
        
        return ans;
        
        
    }
}

//{ Driver Code Starts.

class Driverclass {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(sc.readLine());
        while (n != 0) {
            String input = sc.readLine();
            String[] inputs = input.split(" ");
            int[] arr = new int[inputs.length];

            for (int i = 0; i < inputs.length; i++) {
                arr[i] = Integer.parseInt(inputs[i]);
            }

            ArrayList<Integer> ans = new ArrayList<Integer>();
            ans = new Solution().sortByFreq(arr);
            for (int i = 0; i < ans.size(); i++) System.out.print(ans.get(i) + " ");
            System.out.println();
            n--;
        }
    }
}

// } Driver Code Ends