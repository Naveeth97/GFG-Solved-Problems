/*
class Node{
    int data;
    Node left;
    Node right;
    Node(int data){
        this.data = data;
        left=null;
        right=null;
    }
}

*/
class Solution {
    public boolean isSymmetric(Node root) {
        // Code here
        if (root == null) {
            return true;
        }

        // Use a queue to store nodes for comparison
        Queue<Node> q = new LinkedList<>();

        // Initialize the queue with the left and right subtrees
        q.offer(root.left);
        q.offer(root.right);

        while (!q.isEmpty()) {
          
            Node node1 = q.poll();
            Node node2 = q.poll();

            // If both nodes are null, continue to the next pair
            if (node1 == null && node2 == null) {
                continue;
            }

            // If one node is null and the other is not, 
            // or the nodes' data do not match
            // then the tree is not symmetric
            if (node1 == null || node2 == null || 
                node1.data != node2.data) {
                return false;
            }

            // Enqueue children in opposite order to compare them
            q.offer(node1.left);
            q.offer(node2.right);
            q.offer(node1.right);
            q.offer(node2.left);
        }

        // If the loop completes without 
        // returning false, the tree is symmetric
        return true;
    }
}