class Solution {
    public int solution(int h1, int m1, int s1, int h2, int m2, int s2) {
        int answer = 0;

        int hPerSecond = 1;
        int mPerSecond = 12;
        int sPerSecond = 720;
        
        int hourHand = (h1 * 3600 + m1 * 60 + s1) * hPerSecond;
        int minuteHand = (m1 * 60 + s1) * mPerSecond;
        int secondHand = s1 * sPerSecond;
        
        if (hourHand >= 43200) {
            hourHand = hourHand - 43200;
        }
        
        int start = h1 * 3600 + m1 * 60 + s1;
        int end = h2 * 3600 + m2 * 60 + s2;
        

        
        if (secondHand == minuteHand) {
            answer += 1;
        }

        if (secondHand == hourHand) {
            answer += 1;
            if (minuteHand == hourHand) {
                answer -= 1;
            }
        }

        for (int i = start; i < end; i++) {
            
            secondHand += sPerSecond;
            minuteHand += mPerSecond;
            hourHand += hPerSecond;
            

            if (secondHand - 708 < minuteHand && minuteHand <= secondHand) {
                answer += 1;

            }
            
            if (secondHand - 719 < hourHand && hourHand <= secondHand) {
                answer += 1;

                if (minuteHand == hourHand) {
                    answer -= 1;
                }   
            }
            
            secondHand = secondHand == 43200 ? 0 : secondHand;
            minuteHand = minuteHand == 43200 ? 0 : minuteHand;
            hourHand = hourHand == 43200 ? 0 : hourHand;
        }
        
        
        return answer;
    }
}