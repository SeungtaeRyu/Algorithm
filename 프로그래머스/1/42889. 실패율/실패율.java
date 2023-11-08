import java.util.*;

class Solution {
    public int[] solution(int N, int[] stages) {
        Map<Integer, Integer> failCount = new HashMap<>();
        Map<Integer, Integer> reachCount = new HashMap<>();
        int count = stages.length;
        List<List<Object>> answerList = new ArrayList<>();
        int[] answer = new int[N];
        
        for(int i = 1; i < N+2; i++) failCount.put(i, 0);
        for(int stage: stages) failCount.put(stage, failCount.get(stage)+1);
        for(int i = 1; i < N+2; i++) {
            reachCount.put(i, count);
            count -= failCount.get(i);
        }
        
        
        for(int i = 1; i < N+1; i++) {
            if (reachCount.get(i) == 0) {
                answerList.add(new ArrayList<>(Arrays.asList(0.0, i)));
            } else {
                answerList.add(new ArrayList<>(
                Arrays.asList((double) failCount.get(i) / reachCount.get(i), i)));
            }
            
        }
        
        
        answerList.sort(Comparator.<List<Object>, Double>comparing(list -> (double) list.get(0))
                        .reversed()
                        .thenComparing(list -> (Integer) list.get(1)));
        
        for(int i = 1; i < N+1; i++) answer[i-1] = (Integer) answerList.get(i-1).get(1);
        
        
        
        return answer;
    }
}