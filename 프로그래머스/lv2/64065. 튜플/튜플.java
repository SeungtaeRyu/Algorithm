import java.util.Arrays;
import java.util.Comparator;

class Solution {
    public int[] solution(String s) {
		String substringS = s.substring(2, s.length() - 2);
		String[] splitString = substringS.split("},\\{");
		Arrays.sort(splitString, Comparator.comparing(String::length));

		int[] answer = new int[splitString.length];

		for (int i = 0; i < splitString.length; i++) {
//			System.out.println("ss = " + splitString[i]);
			// 쉼표로 문자열 분할
			String[] parts = splitString[i].split(",");

			// int 배열 생성
			int[] intArray = new int[parts.length];

			// 문자열을 int로 변환하여 배열에 저장
			for (int j = 0; j < parts.length; j++) {
				intArray[j] = Integer.parseInt(parts[j]);
			}

			for (int num: intArray) {

				if ( !isContain(answer, num)) {
					answer[i] = num;
				}
			}
		}

		return answer;
	}


	private boolean isContain(int[] answer, int character) {
		for (int i = 0; i < answer.length; i++) {
			if (answer[i] == character) {
				return true;
			}
		}
		return false;
	}
}