import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while(true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			if (n == 0) break;
			String[] arr = new String[n];
			StringBuilder sb = new StringBuilder();
			for (int i = 0; i < n; i++) {
				arr[i] = st.nextToken();
			}
			dfs(arr, 0, 0, sb, n);
			System.out.println();
		}

	}


	private static void dfs(String[] arr, int i, int n, StringBuilder sb, int max) {
		if(n == 6) {
			System.out.println(sb);
		} else {
			if(i == max) {
				return;
			}
			int startIndex = sb.length();
			sb.append(arr[i]).append(" ");
			dfs(arr, i + 1, n + 1, sb, max);
			sb.delete(startIndex, sb.length());
			dfs(arr, i + 1, n, sb, max);
		}
	}
}