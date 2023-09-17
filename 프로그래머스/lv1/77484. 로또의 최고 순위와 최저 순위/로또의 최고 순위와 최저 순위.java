import java.util.*;
import java.util.stream.Collectors;

class Solution {
	public int[] solution(int[] lottos, int[] win_nums) {
		Set<Integer> winNums = Arrays.stream(win_nums).boxed().collect(Collectors.toSet());
		int winNumsCount = (int) Arrays.stream(lottos).filter(winNums::contains).count();
		int zeroCount = (int) Arrays.stream(lottos).filter(i -> i == 0).count();

		int[] answer = {Math.min(7-winNumsCount-zeroCount, 6) , Math.min(7-winNumsCount, 6)};
		return answer;
	}
}