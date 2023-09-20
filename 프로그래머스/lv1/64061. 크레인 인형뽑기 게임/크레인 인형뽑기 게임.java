import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int height = board.length;
        Stack<Integer> basket = new Stack();
        for(int i: moves) {
            for(int j = 0; j < height; j++) {
                if (board[j][i-1] != 0) {
                    int value = board[j][i-1];
                    board[j][i-1] = 0;
                    
                    if(!basket.isEmpty() && basket.peek() == value) {
                        basket.pop();
                        answer += 2;
                    } else {
                        basket.push(value);
                    }
                    break;
                }
            }
        }
        return answer;
    }
}