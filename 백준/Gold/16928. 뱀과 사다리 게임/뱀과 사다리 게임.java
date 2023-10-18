import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Main test = new Main();

    }

    public Main() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer stk = new StringTokenizer(br.readLine(), " ");

        int n = Integer.parseInt(stk.nextToken());
        int m = Integer.parseInt(stk.nextToken());

        Map<Integer,Integer> ladder = new HashMap<>();
        Map<Integer,Integer> snake = new HashMap<>();

        for (int i = 0; i < n; i++) {
            stk = new StringTokenizer(br.readLine(), " ");

            ladder.put(Integer.parseInt(stk.nextToken()),Integer.parseInt(stk.nextToken()));
        }

        for (int i = 0; i < m; i++) {
            stk = new StringTokenizer(br.readLine(), " ");
            snake.put(Integer.parseInt(stk.nextToken()),Integer.parseInt(stk.nextToken()));
        }


        System.out.println(solution(ladder, snake));

    }

    private int solution( Map<Integer,Integer> ladder,  Map<Integer,Integer> snake) {


        int[] field = new int[101];
        Arrays.fill(field,Integer.MAX_VALUE);
        //param : cur_loc , move_cnt
        Queue<IntPair> queue = new LinkedList<>();
        queue.add(new IntPair(1,0));
        field[1] = 0;

        while (!queue.isEmpty()){

            IntPair cur_info = queue.poll();
            //System.out.println("현재 위치 : \t" +cur_info.left+ "\t cnt :" +cur_info.right);
            if( cur_info.left == 100){
                break;
            }

            int move_cnt = cur_info.right+1;

            for (int i = 6 ; i >0 ;i--){
                int next_cur = cur_info.left;
                next_cur+=i;
                if(next_cur > 100){
                    continue;
                }
                //뱀을 타고 내려가야만 하는 경우도 고려해야함
                if(snake.containsKey(next_cur)){
                    next_cur = snake.get(next_cur);
                }

                //사다리를 탈 수 있다면 탄 위치로
                else if (ladder.containsKey(next_cur)){
                    //System.out.println("사다리 탐!!!!");
                    next_cur = ladder.get(next_cur);

                }

                //해당 필드에 있는 값보다 지금값이 더 작을때만 작동
                if(field[next_cur] > move_cnt){
                    field[next_cur] = move_cnt;
                    queue.add(new IntPair(next_cur,move_cnt));
                }

            }
        }



        return field[100];
    }



    class IntPair{
        Integer left;
        Integer right;

        public IntPair(Integer left, Integer right) {
            this.left = left;
            this.right = right;
        }
    }

}