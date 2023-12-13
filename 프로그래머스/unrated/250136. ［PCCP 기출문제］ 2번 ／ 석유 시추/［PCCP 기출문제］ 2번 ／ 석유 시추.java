import java.util.Arrays;
class Solution {
    private int minY;
    private int maxY;
    private int n;
    private int m;
    private int count = 0;
    private boolean[][] visited;
    public int solution(int[][] land) {
        // int answer = 0;
        n = land.length;
        m = land[0].length;
        visited = new boolean[n][m];
        int[] answer = new int[m];
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && land[i][j] == 1) {
                    minY = j;
                    maxY = j;
                    dfs(i, j, land);
                    minY = Math.max(0, minY);
                    maxY = Math.min(m-1, maxY);
                    for (int k = minY; k <= maxY; k++) {
                        answer[k] += count;
                    }
                    count = 0;
                }
            }
        }
        
        return Arrays.stream(answer).max().orElse(0);
    }
    
    private void dfs(int x, int y, int[][] land) {
        count += 1;
        visited[x][y] = true;
        minY = Math.min(minY, y);
        maxY = Math.max(maxY, y);
        if (x > 0 && land[x-1][y] == 1 && !visited[x-1][y]) {
            dfs(x-1, y, land);
        }
        if (x < n-1 && land[x+1][y] == 1 && !visited[x+1][y]) {
            dfs(x+1, y, land);
        }
        if (y > 0 && land[x][y-1] == 1 && !visited[x][y-1]) {
            dfs(x, y-1, land);
        }
        if (y < m-1 && land[x][y+1] == 1 && !visited[x][y+1]) {
            dfs(x, y+1, land);
        }
    }
    
}