import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
		int answer = 0;
		int maxsize = 102;
		int[][] map = new int[maxsize][maxsize];
		int[][] map2 = new int[maxsize][maxsize];
		int[][] visited = new int[maxsize][maxsize];

		Queue<int[]> bfs = new LinkedList<>();


		for (int[] ract: rectangle) {
			for (int i = ract[0] * 2 ; i < ract[2] * 2 + 1; i++ ){
				for (int j = ract[1] * 2 ; j < ract[3] * 2 + 1; j++) {
					map[i][j] = 1;
				}
			}
		}

		for (int i = 1; i < maxsize -1; i++) {
			for (int j = 1; j < maxsize -1; j++) {
				if (map[i-1][j-1] == 1 && map[i-1][j+1] == 1 && map[i+1][j-1] == 1 && map[i+1][j+1] == 1 && map[i][j-1] == 1 && map[i][j+1] == 1 && map[i-1][j] == 1 && map[i+1][j] == 1) {

				} else {
					map2[i][j] = map[i][j];
				}
			}
		}

		bfs.add(new int[] {characterX*2, characterY*2});
		visited[characterX*2][characterY*2] = 1;
		int[][] direction = new int[][] {{0, -1}, {0, 1}, {-1, 0}, {1, 0}};
		while (!bfs.isEmpty()) {
            answer += 1;
		
			int[] cur = bfs.poll();
			if (cur[0] == itemX*2 && cur[1] == itemY*2 ) {
				break;
			}
			for(int[] d: direction){
				int nx = cur[0] + d[0];
				int ny = cur[1] + d[1];
				if ( nx >=0 && nx <= maxsize && ny >= 0 && ny <= maxsize && visited[nx][ny] == 0 && map2[nx][ny] == 1) {
					bfs.add(new int[] {nx, ny});
					visited[nx][ny] = 1;
				}
			}
		}



		return answer / 4;
    }
}