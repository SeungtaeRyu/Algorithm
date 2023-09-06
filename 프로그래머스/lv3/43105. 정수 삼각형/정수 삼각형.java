import java.util.Arrays;

class Solution {
    public int solution(int[][] triangle) {
        int triangleLength = triangle.length;   
		int[][] dp = new int[triangleLength][triangleLength+1];

		dp[0][1] = triangle[0][0];
		for (int i = 1; i < triangleLength; i++) {
			for (int j = 1; j < i+2; j ++) {
				dp[i][j] = Math.max(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j - 1];
			}
		}

		return Arrays.stream(dp[triangleLength-1]).max().getAsInt();
    }
}