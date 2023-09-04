import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;


public class Main {


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int[] visited = new int[k+1];
		Arrays.fill(visited, -1);
		Queue<Integer> queue = new LinkedList<>();
		queue.add(n);
		visited[n] = 0;


		while (visited[k] == -1) {

			int current = 0;
			if (queue.peek() != null) {
				current = queue.poll();
			}

			if (current * 2 <= k && visited[current * 2] == -1) {
				visited[current * 2] = visited[current] + 1;
				queue.add(current * 2);
			}

			if (current + 1 <= k && visited[current + 1] == -1) {
				visited[current + 1] = visited[current] + 1;
				queue.add(current + 1);
			}
		}

		System.out.println(visited[k]);

	}
}
