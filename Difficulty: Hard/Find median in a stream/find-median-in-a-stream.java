//{ Driver Code Starts
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine(); // Consume the newline character

        while (t-- > 0) {
            String s = sc.nextLine();
            String[] parts = s.split(" ");
            int[] nums = new int[parts.length];
            for (int i = 0; i < parts.length; i++) {
                nums[i] = Integer.parseInt(parts[i]);
            }
            Solution ob = new Solution();
            ArrayList<Double> ans = ob.getMedian(nums);
            for (double i : ans) {
                System.out.printf("%.1f ", i);
            }
            System.out.println();
            System.out.println("~");
        }
        sc.close();
    }
}

// } Driver Code Ends


class Solution {
    public ArrayList<Double> getMedian(int[] arr) {
        // code here
        
        ArrayList<Double> medianArr = new ArrayList<>();
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a, b) -> arr[a] - arr[b]);
        
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a, b) -> arr[b] - arr[a]);
        
        
        for (int i = 0; i < arr.length; i++) {
            
            minHeap.add(i);
            maxHeap.add(minHeap.poll());
            
            balanceHeap(minHeap, maxHeap);
            
            if (i % 2 == 0) {
                medianArr.add((double)arr[minHeap.peek()]);
            } else {
                medianArr.add((double)(arr[minHeap.peek()] + arr[maxHeap.peek()]) / 2);
            }
            
        }
        
        return medianArr;
    }
    
    private void balanceHeap(PriorityQueue<Integer> minHeap, PriorityQueue<Integer> maxHeap) {
        
        
        if (maxHeap.size() > minHeap.size()) {
            minHeap.add(maxHeap.poll());
        }
        
    }
}