import java.util.*;
class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        Map<String, Map<String, Integer>> info = new HashMap<String, Map<String, Integer>>();
        String GC = "GIVE_COUNT";
        String TC = "TAKE_COUNT";
        String SCALE = "PRESENT_SCALE";
        // 자료구조 생성
        for(int i = 0; i < friends.length; i++) {
            info.put(friends[i], new HashMap<>());
            info.get(friends[i]).put(GC, 0);
            info.get(friends[i]).put(TC, 0);
            for(int j = 0; j < friends.length; j++) {
                if(i != j) {
                    info.get(friends[i]).put(friends[j], 0);
                }
            }
        }
        // 이번달 선물 개수 카운팅
        for(String gift: gifts) {
            String[] toFrom = gift.split(" ");
            String giver = toFrom[0];
            String taker = toFrom[1];
            info.get(giver).put(GC, info.get(giver).get(GC) + 1);
            info.get(taker).put(TC, info.get(taker).get(TC) + 1);
            info.get(giver).put(taker, info.get(giver).get(taker) + 1);
        }
        
        // 선물지수 계산
        for(int i = 0; i < friends.length; i++) {
            info.get(friends[i]).put(SCALE, info.get(friends[i]).get(GC) - info.get(friends[i]).get(TC));
        }
        
        // 다음달 선물 계산
        for(int i = 0; i < friends.length; i++) {
            int tempAnswer = 0;
            for(int j = 0; j < friends.length; j++) {
                if(i != j) {
                    // a 가 b 보다 선물을 많이 줬을 때
                    if(info.get(friends[i]).get(friends[j]) > info.get(friends[j]).get(friends[i])) {
                        tempAnswer += 1;
                    }
                    // 선물을 준 갯수가 같을 때
                    else if(info.get(friends[i]).get(friends[j]) == info.get(friends[j]).get(friends[i])) {
                        if(info.get(friends[i]).get(SCALE) > info.get(friends[j]).get(SCALE)) {
                            tempAnswer += 1;
                        }
                    }
                    
                }
            }
            answer = Math.max(answer, tempAnswer);
        }
        
        return answer;
    }
}