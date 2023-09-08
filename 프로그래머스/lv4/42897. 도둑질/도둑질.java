public class Solution {
	public int solution(int[] money) {
		int answer = 0;

		int[] dp1 = new int[money.length];
		int[] dp2 = new int[money.length];

		if (money.length == 3) {
			for (int i = 0; i < money.length; i++) {
				if (money[i] > answer) {
					answer = money[i];
				}
			}
			return answer;
		} else {
			/**
			 * 첫번째 집을 고를 경우 마지막집을 고르지 않고 최대값 찾음
			 */
			dp1[0] = money[0];
			dp1[1] = money[1];
			dp1[2] = money[0] + money[2];
			for ( int i = 3; i < money.length-1; i++) {
				dp1[i] = Math.max(dp1[i-3], dp1[i-2]) + money[i];
			}
			for (int i = 1; i < money.length; i++) {
				if (dp1[i] > answer) {
					answer = dp1[i];
				}
			}

			/**
			 * 두번째 집을 고를 경우 마지막집까지 탐색하여 최대값 찾음
			 */
			dp2[1] = money[1];
			dp2[2] = money[2];
			for ( int i = 3; i < money.length; i++) {
				dp2[i] = Math.max(dp2[i-3], dp2[i-2]) + money[i];
			}
			for (int i = 0; i < money.length; i++) {
				if (dp2[i] > answer) {
					answer = dp2[i];
				}
			}

			return answer;

		}

	}

}
