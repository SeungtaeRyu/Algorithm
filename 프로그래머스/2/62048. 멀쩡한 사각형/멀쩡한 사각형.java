class Solution {
    public long solution(int w, int h) {
        long answer = (long) w * h;
        
        int gcd = gcd(h, w);
        int ww = w / gcd; // 분모
        int hh = h / gcd; // 분자
        // System.out.println(ww + " " + hh);
        // 2 / 3
        int a = w / ww; // 가로길이 / 분모
        
        answer -= gcd * (hh+ww-1);
        
        
        return answer;
    }
    
    // 최대 공약수(Greatest Common Divisor)를 계산하는 함수
    private static int gcd(int a, int b) {
        if (b == 0) {
            return a;
        }
        return gcd(b, a % b);
    }
}