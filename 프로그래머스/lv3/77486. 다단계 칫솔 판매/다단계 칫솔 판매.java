import java.util.*;

class Solution {
   public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {

		Map<String, Integer> revenue = new HashMap<>();
		Map<String, String> parent = new HashMap<>();

		for (String s: enroll) {
			revenue.put(s, 0);
		}

		for (int i = 0; i < enroll.length; i++) {
			parent.put(enroll[i], referral[i]);
		}

		for (int i = 0; i < seller.length; i++) {
			updateRevenue(seller[i], amount[i] * 100, revenue, parent);
		}

		
		int[] answer = new int[enroll.length];
		for(int i = 0; i < enroll.length; i++) {
			answer[i] = revenue.get(enroll[i]);
		}

		return answer;
	}


	private void updateRevenue(String child, int amount, Map<String, Integer> revenue, Map<String, String> parent) {
		int childRevenue = revenue.get(child);
		int passMoney = amount / 10;

		revenue.put(child, childRevenue + amount - passMoney);
		if (!Objects.equals(parent.get(child), "-") && passMoney != 0) {
			updateRevenue(parent.get(child), passMoney, revenue, parent);
		}


	}
}