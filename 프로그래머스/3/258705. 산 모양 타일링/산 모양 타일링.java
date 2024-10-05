class Solution {
    public int solution(int n, int[] tops) {
        int answer = 0;
        int[][] DP = new int[n+1][2];
        // DP[*][0] => 마지막이 자유로움
        // DP[*][1] => 마지막이 자유롭지 않음
        DP[0][0] = 1;
        // tops[0] = 0
        if (tops[0] == 0) {
            DP[1][0] = DP[0][0] * 2;
            DP[1][1] = DP[0][0];
        // tops[0] = 1
        } else { 
            DP[1][0] = DP[0][0] * 3;
            DP[1][1] = DP[0][0];    
        }
        System.out.println(DP[1][0] + DP[1][1]);
        for(int i = 1; i < n; i++) {
            int top = tops[i];
            if(top==0) {
                DP[i+1][0] = (DP[i][0] * 2 + DP[i][1]) % 10007;
                DP[i+1][1] = (DP[i][0] + DP[i][1]) % 10007;
            } else {
                DP[i+1][0] = (DP[i][0] * 3 + DP[i][1] * 2) % 10007;
                DP[i+1][1] = (DP[i][0] + DP[i][1]) % 10007;
            }
        }
            
        
        answer = (DP[n][0] + DP[n][1]) % 10007;
        return answer;
    }
}