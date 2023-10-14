import java.util.*;

class Solution {
    public int solution(int[] d, int budget) {
        int answer = 0;
        Arrays.sort(d);
        int i = 0;
        while (budget >=0 && i != d.length) {
            budget -= d[i];
            i += 1;
        }
        answer = budget < 0 ? i-1 : i;
        return answer;
    }
}