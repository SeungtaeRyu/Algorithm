class Solution {
    public int solution(int[] bandage, int health, int[][] attacks) {
        int answer = health; // HP
        int time = 0; // time
        for (int[] attack: attacks) {
            int attackTime = attack[0];
            int attackDamage = attack[1];
            int healthTime = attackTime - time - 1;
            time = attackTime;
            int additionalAmount = healthTime / bandage[0] * bandage[2];
            answer = Math.min(health, answer + healthTime * bandage[1] + additionalAmount);
            answer -= attackDamage;
            if (answer <= 0) {
                return -1;
            }
        }
        
        return answer;
    }
}