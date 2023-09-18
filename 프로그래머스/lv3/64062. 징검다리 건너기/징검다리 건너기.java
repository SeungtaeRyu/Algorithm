
import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
	 public int solution(int[] stones, int k) {
		 int answer = Integer.MAX_VALUE;
		 Deque<Integer> maxValues = new ArrayDeque<>();

		 for (int i = 0; i < stones.length; i++) {
			 while (!maxValues.isEmpty() && maxValues.peekLast() < stones[i]) {
				 maxValues.pollLast();
			 }
			 maxValues.offer(stones[i]);

			 if (i >= k - 1) {
				 answer = Math.min(answer, maxValues.peek());
				 if (stones[i - k + 1] == maxValues.peek()) {
					 maxValues.poll();
				 }
			 }
		 }

		 return answer;
	 }
}