//{ Driver Code Starts
import java.io.*;
import java.lang.*;
import java.util.*;

class Node {
    int data;
    Node next;

    Node(int key) {
        data = key;
        next = null;
    }
}

class ReverseInSize {
    static Node head;

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);

        int t = Integer.parseInt(in.readLine().trim());

        while (t-- > 0) {

            String s[] = in.readLine().trim().split(" ");
            int a1 = Integer.parseInt(s[0]);
            Node head = new Node(a1);
            Node tail = head;
            for (int i = 1; i < s.length; i++) {
                int a = Integer.parseInt(s[i]);
                // addToTheLast(new Node(a));
                tail.next = new Node(a);
                tail = tail.next;
            }

            int k = Integer.parseInt(in.readLine().trim());
            Solution ob = new Solution();
            Node res = ob.reverseKGroup(head, k);
            printList(res, out);
            out.println();

            out.println("~");
        }
        out.close();
    }

    public static void printList(Node node, PrintWriter out) {
        while (node != null) {
            out.print(node.data + " ");
            node = node.next;
        }
    }
}

// } Driver Code Ends


/*node class of the linked list
class Node
{
    int data;
    Node next;
    Node(int key)
    {
        data = key;
        next = null;
    }
}

*/

class Solution {
    public static Node reverseKGroup(Node head, int k) {
        
        Node temp = head, prev = null;
        boolean flag = false;
        
        while (temp != null) {
            Node tempHead = temp;
            
            for (int i = 1; i <= k - 1 && temp != null; i++) {
                temp = temp.next;
            }
            
            Node next = null;
            
            if (temp != null) {
                next = temp.next;
                temp.next = null;
            }
            
            Node rev = reverseLL(tempHead);
            
            if (!flag) {
                flag = true;
                head = rev;
            }
            
            if (prev != null)
                prev.next = rev;
                
            prev = tempHead;
            
            prev.next = next;
            temp = next;
        }
        
        return head;
    }
    
    private static Node reverseLL(Node head) {
        Node temp = head, prev = null;
        
        while (temp != null) {
            Node front = temp.next;
            temp.next = prev;
            prev = temp;
            temp = front;
        }
        
        return prev;
    }
}
