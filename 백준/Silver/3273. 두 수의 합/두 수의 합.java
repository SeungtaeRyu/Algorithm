import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;


public class Main {
	public static void main(String[] args) throws IOException {
		int answer = 0;
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int[] arr = new int[n];
		for(int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(arr);
		int x = Integer.parseInt(br.readLine());


		int start = 0;
		int end = n-1;
		while(start < end) {
			if(arr[start] + arr[end] == x) {
				answer += 1;
				start += 1;
				end -= 1;
			} else if (arr[start] + arr[end] < x) {
				start += 1;
			} else {
				end -= 1;
			}
		}
		System.out.println(answer);
	}
}
