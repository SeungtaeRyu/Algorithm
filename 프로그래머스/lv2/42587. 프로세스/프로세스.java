import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

class Solution {
    public int solution(int[] priorities, int location) {
		int answer = 0;
		Queue<List> queue = new LinkedList<>();
		for (int i = 0; i < priorities.length; i++) {
			queue.add(List.of(priorities[i], i));
		}

		while (true) {
			List<Integer> first = queue.poll();
			int priority = first.get(0);
			int index = first.get(1);
			if (priority >= queue.stream().mapToInt(q -> (int) q.get(0)).max().orElse(Integer.MIN_VALUE)) {
				answer += 1;
				if (index == location) {
					break;
				}
			} else {
				queue.add(first);
			}
		}

		return answer;
	}
}