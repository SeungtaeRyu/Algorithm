import java.util.*;

class Solution {
    public String[] solution(String[] files) {
String[] answer = {};

		Arrays.sort(files, new Comparator<String>() {
			@Override
			public int compare(String o1, String o2) {
				String[] file1 = split(o1);
				String[] file2 = split(o2);

				int isSameHead = file1[0].compareTo(file2[0]);

				if(isSameHead == 0) {
					int num1 = Integer.parseInt(file1[1]);
					int num2 = Integer.parseInt(file2[1]);

					return num1 - num2;
				} else {
					return isSameHead;
				}
			}

			private String[] split(String str){
				String header = "";
				String number = "";
				String footer = "";

				int i = 0;
				while (i < str.length() && !Character.isDigit(str.charAt(i))) {
					header += str.charAt(i);
					i++;
				}

				while (i < str.length() && Character.isDigit(str.charAt(i))) {
					number += str.charAt(i);
					i++;
				}

				footer = str.substring(i);

				String[] file = { header.toLowerCase(), number, footer };

				return file;
			}
		});

		for (String file: files) {
			System.out.println("file = " + file);
		}

		return files;
    }
}