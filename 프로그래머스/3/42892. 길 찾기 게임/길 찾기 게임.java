import java.util.*;

class Solution {
    private static int[][] answer = new int[2][];
	List<Integer> preOrder = new ArrayList<>();
	List<Integer> postOrder = new ArrayList<>();
	static class Node {
		int level;
		int value;
		int x;
		int y;
		Node parent = null;
		Node left = null;
		Node right = null;


		public Node(int x, int y, int value, int level) {
			this.x = x;
			this.y = y;
			this.level = level;
			this.value = value;
		}

	}

	public int[][] solution(int[][] nodeinfo) {
		List<List<Integer>> nodeInfoList = new ArrayList<>();
		int level = 0;

		int value = 1;

		for (int[] nodeInfo: nodeinfo) {
			nodeInfoList.add(new ArrayList<>(Arrays.asList(nodeInfo[0],nodeInfo[1], value)));
			value += 1;
		}

		nodeInfoList.sort(Comparator.<List<Integer>>comparingInt(list -> list.get(1)).reversed()
			.thenComparingInt(list -> list.get(0)));

		Node root = new Node(nodeInfoList.get(0).get(0), nodeInfoList.get(0).get(1), nodeInfoList.get(0).get(2), level);
		int y = root.y;
		for (int i = 1; i < nodeInfoList.size(); i++) {
			if (y != nodeInfoList.get(i).get(1)) {
				level += 1;
				y = nodeInfoList.get(i).get(1);
			}
			Node node = new Node(nodeInfoList.get(i).get(0), nodeInfoList.get(i).get(1), nodeInfoList.get(i).get(2), level);
			findParent(root, node);
		}

		preOrder(root);
		postOrder(root);

		answer[0] = preOrder.stream().mapToInt(Integer::intValue).toArray();
		answer[1] = postOrder.stream().mapToInt(Integer::intValue).toArray();

		return answer;
	}

	private void preOrder(Node node) {
		preOrder.add(node.value);
		if (node.left != null) {
			preOrder(node.left);
		}

		if (node.right != null) {
			preOrder(node.right);
		}
	}

	private void postOrder(Node node) {
		if (node.left != null) {
			postOrder(node.left);
		}

		if (node.right != null) {
			postOrder(node.right);
		}
		postOrder.add(node.value);
	}


	private void findParent(Node parent, Node node) {
		if (parent.level + 1 == node.level) {
			node.parent = parent;
			if (node.x < parent.x) {
				parent.left = node;
			} else {
				parent.right = node;
			}
		} else if (node.x < parent.x) {
			findParent(parent.left, node);
		} else {
			findParent(parent.right, node);
		}
	}
}