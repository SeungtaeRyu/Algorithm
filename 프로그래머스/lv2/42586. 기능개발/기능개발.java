import java.util.ArrayList;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
		int index = 0;

		while (index < progresses.length) {
			// 진도 업데이트
			for (int i = index; i < progresses.length; i++) {
				progresses[i] += speeds[i];
			}

			// 배포할 작업 확인
			int complete = 0;
			while (index < progresses.length && progresses[index] >= 100) {
				index += 1;
				complete += 1;
			}

			if (complete > 0) {
				answer.add(complete);
			}
		}

		return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}