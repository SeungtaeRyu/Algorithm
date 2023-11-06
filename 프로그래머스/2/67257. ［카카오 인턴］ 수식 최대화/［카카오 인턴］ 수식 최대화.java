import java.util.*;

class Solution {
    private List<List<String>> permutataion;
	public long solution(String expression) {
		long answer = 0;
		List<String> expressionSplit = new ArrayList<>();
		StringBuilder temp = new StringBuilder();
		Set<String> operatorSet = new HashSet<>();

		// 연산자 기준으로 잘라서 스트링으로 저장, set에 연산자 저장
		for (int i = 0; i < expression.length(); i++) {
			if (Character.isDigit(expression.charAt(i))) {
				temp.append(expression.charAt(i));
			} else {
				expressionSplit.add(temp.toString());
				expressionSplit.add(String.valueOf(expression.charAt(i)));
				temp.delete(0, temp.length());
				operatorSet.add(String.valueOf(expression.charAt(i)));
			}
		}
		expressionSplit.add(temp.toString());

		// 순열 구하기
		List<String> operatorList = new ArrayList<>(operatorSet);
		permutataion = new ArrayList<>();
		boolean[] visited = new boolean[operatorSet.size()];
		savePermutation(visited, operatorList, 0, operatorSet.size(), new ArrayList<>());

		// 순열마다 계산해보기
		for(List<String> per: permutataion) {
			List<String> tempExpression = new ArrayList<>(expressionSplit);
			for(String p: per) {
				int index = 0;
				while (index < tempExpression.size()) {
					if (tempExpression.get(index).equals(p)) {
						if (p.equals("-")) {
							tempExpression.set(index, minus(tempExpression.get(index-1), tempExpression.get(index+1)));
							tempExpression.remove(index-1);
							tempExpression.remove(index);
						} else if (p.equals("+")) {
							tempExpression.set(index, plus(tempExpression.get(index-1), tempExpression.get(index+1)));
							tempExpression.remove(index-1);
							tempExpression.remove(index);
						} else if (p.equals("*")) {
							tempExpression.set(index, multiplication(tempExpression.get(index-1), tempExpression.get(index+1)));
							tempExpression.remove(index-1);
							tempExpression.remove(index);
						}
					} else {
						index += 1;
					}
				}
			}
			answer = Math.max(answer, Math.abs(Long.parseLong(tempExpression.get(0))));
		}
		return answer;
	}
	public void savePermutation(boolean[] visited, List<String> operatorList, int depth, int n, List<String> result) {
		if (depth == n) {
			permutataion.add(new ArrayList<>(result));
		} else {
			for (int i = 0; i < operatorList.size(); i++) {
				if (!visited[i]) {
					visited[i] = true;
					result.add(operatorList.get(i));
					savePermutation(visited, operatorList, depth + 1, n, result);
					visited[i] = false;
					result.remove(operatorList.get(i));
				}
			}
		}
	}

	public String plus(String x, String y) {
		long xx = Long.parseLong(x);
		long yy = Long.parseLong(y);
		return Long.toString(xx + yy);
	}
	public String minus(String x, String y) {
		long xx = Long.parseLong(x);
		long yy = Long.parseLong(y);
		return Long.toString(xx - yy);
	}
	public String multiplication(String x, String y) {
		long xx = Long.parseLong(x);
		long yy = Long.parseLong(y);
		return Long.toString(xx * yy);
	}
    
}