import java.util.Arrays;

class Solution {
    private int[][][] visited;
	public int solution(int[][] board) {
		int answer = 0;
		visited = new int[board.length][board.length][4];

		for (int i = 0; i < board.length; i++) {
			for (int j = 0; j < board.length; j++) {
				Arrays.fill(visited[i][j], Integer.MAX_VALUE);
			}
		}

		dfs(board, 0, 0, 0, 0);
		dfs(board, 0, 0, 3, 0);

		return Math.min(visited[board.length-1][board.length-1][0], visited[board.length-1][board.length-1][3]);
	}

	private void dfs(int[][] board, int x, int y, int direction, int value) {
		// direction 은 상하좌우 [상, 하, 좌, 우]
		// 상 x 증가
		if (x+1 < board.length && board[x+1][y] == 0) {
			int cost = direction == 0 || direction == 1 ? 100 : 600;
			if (value + cost < visited[x+1][y][0]) {
				visited[x+1][y][0] = value + cost;
				dfs(board, x+1, y, 0, value + cost);
			}
		}
		// 하 x 감소
		if (x-1 >= 0 && board[x-1][y] == 0) {
			int cost = direction == 0 || direction == 1 ? 100 : 600;
			if (value + cost < visited[x-1][y][1]) {
				visited[x-1][y][1] = value + cost;
				dfs(board, x-1, y, 1, value + cost);
			}
		}
		// 좌 y 감소
		if (y-1 >= 0 && board[x][y-1] == 0) {
			int cost = direction == 2 || direction == 3 ? 100 : 600;
			if (value + cost < visited[x][y-1][2]) {
				visited[x][y-1][2] = value + cost;
				dfs(board, x, y-1, 2, value + cost);
			}
		}
		// 우 y 증가
		if (y+1 < board.length && board[x][y+1] == 0) {
			int cost = direction == 2 || direction == 3 ? 100 : 600;
			if (value + cost < visited[x][y+1][3]) {
				visited[x][y+1][3] = value + cost;
				dfs(board, x, y+1, 3, value + cost);
			}
		}
	}
}