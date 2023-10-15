import java.util.*;

class Solution {
    public int solution(int[] cookie) {
        int answer = 0;
        int sum = Arrays.stream(cookie).boxed().mapToInt(Integer::intValue).sum();
        
        for (int i = 1; i < cookie.length; i++) {
            int aIndex = i-1;
            int bIndex = i;
            int sumA = cookie[aIndex];
            int sumB = cookie[bIndex];

            while (true) {
                
                if (sumA == sumB) {
                    answer = Math.max(answer, sumA);
                    aIndex -= 1;
                    bIndex += 1;
                    if (aIndex < 0 || bIndex == cookie.length) {
                        break;
                    }
                    sumA += cookie[aIndex];
                    sumB += cookie[bIndex];
                } else if (sumA < sumB) {
                    aIndex -= 1;
                    if (aIndex < 0) {
                        break;
                    }
                    sumA += cookie[aIndex];
                } else if (sumA > sumB) {
                    bIndex += 1;
                    if (bIndex == cookie.length) {
                        break;
                    }
                    sumB += cookie[bIndex];
                }
            }
        }
        return answer;
    }
}