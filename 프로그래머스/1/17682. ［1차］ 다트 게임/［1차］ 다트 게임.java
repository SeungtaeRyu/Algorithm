class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        int prev = 0;
        int cur = 0;
        StringBuilder sb = new StringBuilder();
        int i = 0;
        boolean isNumber = false;
        while (i < dartResult.length()) {
            char c = dartResult.charAt(i);
            // 스타상, 아차상 처리
            if (c == '*') {
                answer += prev + cur;
                prev += prev;
                cur += cur;
                i += 1;
                continue;
            } else if (c == '#') {
                cur -= 2 * cur;
                answer += 2 * cur;
                i += 1;
                continue;
            }
            
            // 숫자 
            if (Character.isDigit(c)) {
                if (!isNumber) {
                    sb = new StringBuilder();
                    isNumber = true;
                }
                sb.append(c);
                i += 1;
            
            // S, D, T
            } else {
                isNumber = false;
                prev = cur;
                cur = Integer.parseInt(sb.toString());
                if (c == 'S') {
                    answer += cur;  
                } else if (c == 'D') {
                    cur = cur * cur;
                    answer += cur;
                } else if (c == 'T') {
                    cur = cur * cur * cur;
                    answer += cur;
                }
                i += 1;
            }
        }
        return answer;
    }
}