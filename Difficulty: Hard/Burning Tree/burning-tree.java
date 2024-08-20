//{ Driver Code Starts
//Initial Template for Java


import java.util.LinkedList;
import java.util.Queue;
import java.io.*;
import java.util.*;

class Node {
	int data;
	Node left;
	Node right;

	Node(int data) {
		this.data = data;
		left = null;
		right = null;
	}
}

class GfG {

	static Node buildTree(String str) {

		if (str.length() == 0 || str.charAt(0) == 'N') {
			return null;
		}

		String ip[] = str.split(" ");
		// Create the root of the tree
		Node root = new Node(Integer.parseInt(ip[0]));
		// Push the root to the queue

		Queue<Node> queue = new LinkedList<>();

		queue.add(root);
		// Starting from the second element

		int i = 1;
		while (queue.size() > 0 && i < ip.length) {

			// Get and remove the front of the queue
			Node currNode = queue.peek();
			queue.remove();

			// Get the current node's value from the string
			String currVal = ip[i];

			// If the left child is not null
			if (!currVal.equals("N")) {

				// Create the left child for the current node
				currNode.left = new Node(Integer.parseInt(currVal));
				// Push it to the queue
				queue.add(currNode.left);
			}

			// For the right child
			i++;
			if (i >= ip.length)
				break;

			currVal = ip[i];

			// If the right child is not null
			if (!currVal.equals("N")) {

				// Create the right child for the current node
				currNode.right = new Node(Integer.parseInt(currVal));

				// Push it to the queue
				queue.add(currNode.right);
			}
			i++;
		}

		return root;
	}

	static void printInorder(Node root) {
		if (root == null)
			return;

		printInorder(root.left);
		System.out.print(root.data + " ");

		printInorder(root.right);
	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int t = Integer.parseInt(br.readLine());

		while (t > 0) {
			String s = br.readLine();
			int target = Integer.parseInt(br.readLine());
			Node root = buildTree(s);

			Solution g = new Solution();
			System.out.println(g.minTime(root, target));
			t--;

		}
	}
}



// } Driver Code Ends


//User function Template for Java

class Solution
{
    /*class Node {
    	int data;
    	Node left;
    	Node right;
    
    	Node(int data) {
    		this.data = data;
    		left = null;
    		right = null;
    	}
    }*/
    
    static Node markParents(Map<Node, Node> parentNode, Node root, int target) {
        
        Queue<Node> queue = new LinkedList<>();
        queue.add(root);
        
        Node start = null;
        
        while (!queue.isEmpty()) {
            
            Node temp = queue.poll();
            
            if (temp.data == target) start = temp;
            
            if (temp.left != null) {
                
                queue.add(temp.left);
                parentNode.put(temp.left, temp);
            }
            
            if (temp.right != null) {
                
                queue.add(temp.right);
                parentNode.put(temp.right, temp);
            }
        }
        return start;
    }
    
    public static int minTime(Node root, int target) 
    {
        // Your code goes here
        Map<Node, Node> parentNode = new HashMap<>();
        
        Node targets = markParents(parentNode, root, target);
        
        Queue<Node> queue = new LinkedList<>();
        
        queue.add(targets);
        
        Map<Node, Node> visited = new HashMap<>();
        
        visited.put(targets, targets);
        
        int time = 0;
        
        while (!queue.isEmpty()) {
            
            int size = queue.size();
            int encounter = 0;
            
            for (int i = 0; i < size; i++) {
                
                Node current = queue.poll();
                
                if (current.left != null && visited.get(current.left) == null) {
                    
                    queue.add(current.left);
                    visited.put(current, current.left);
                    encounter = 1;
                }
                
                if (current.right != null && visited.get(current.right) == null) {
                    
                    queue.add(current.right);
                    visited.put(current, current.right);
                    encounter = 1;
                }
                
                if (parentNode.get(current) != null && visited.get(parentNode.get(current)) == null) {
                    
                    queue.add(parentNode.get(current));
                    visited.put(parentNode.get(current), current);
                    encounter = 1;
                }
            }
            
            if (encounter == 1) {
                time++;
            }
            
        }
        
        return time;
    }
}