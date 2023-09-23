import java.util.*;

class Solution {
    public int solution(String[] user_id, String[] banned_id) {
		Map<String, List<String>> candidate = new HashMap<>();

		for (String banUser: banned_id) {
			candidate.put(banUser, new ArrayList<>());
			for (String user: user_id) {
				if (banUser.length() == user.length()) {
					int idLength = banUser.length();
					boolean equals = true;
					for (int i = 0; i < idLength; i++) {
						if (!String.valueOf(banUser.charAt(i)).equals("*") && !String.valueOf(banUser.charAt(i)).equals(String.valueOf(user.charAt(i)))) {
							equals = false;
							break;
						}
					}
					if (equals) {
						candidate.get(banUser).add(user);
					}
				}
			}
		}

		Set<Set<String>> answerList = new HashSet<>();

		int n = banned_id.length;
		findAllCombination(answerList, candidate, banned_id, new HashSet<>(), 0, n);

		System.out.println("answerList = " + answerList);


		return answerList.size();
	}


	private void findAllCombination(Set<Set<String>> answerList, Map<String, List<String>> candidate, String[] banned_id, Set<String> set, int i, int n) {
		if (i == n-1) {
			for (String id: candidate.get(banned_id[i])) {
				if (!set.contains(id)) {
					set.add(id);
					answerList.add(new HashSet<>(set));
					set.remove(id);
				}
			}
		} else {
			for (String id: candidate.get(banned_id[i])) {
				if (!set.contains(id)) {
					set.add(id);
					findAllCombination(answerList, candidate, banned_id, set, i+1, n);
					set.remove(id);
				}
			}
		}
	}
}