class Solution {
    public int solution(String s) {
        int answer = s.length();
        
        for (int i = 1; i <= s.length() / 2; i++) {
            
            int count = 0;
            int index = 0;
            StringBuilder sb = new StringBuilder();
            String prevString = s.substring(0, i);
            String tempString = "";
            
            while (index < s.length()) {
                // 현재 단어 검색
                if (index + i >= s.length()) {
                    tempString = s.substring(index);
                } else {
                    tempString = s.substring(index, index + i);
                }
                
                // 이전 단어와 같으면 패스
                if(prevString.equals(tempString)) {
                    index += i;
                    count += 1;
                    
                // 이전 단어와 다르면 정답에 개수 + 문자열 넣고 이전 단어 초기화
                } else {
                    if (count != 1) {
                        sb.append(String.valueOf(count));
                    }
                    sb.append(prevString);
                    
                    prevString = new String(tempString);
                    count = 1;
                    index += i;
                }
            }
            if (count != 1) {
                sb.append(String.valueOf(count));
            }
            sb.append(prevString);
            answer = Math.min(answer, sb.toString().length());
        }
        return answer;
    }
}