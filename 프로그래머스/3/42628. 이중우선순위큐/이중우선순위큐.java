import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.NoSuchElementException;

class Solution {
    public int[] solution(String[] operations) {
		int[] answer = new int[2];
		int[] tq = new int[operations.length];
		String[] look = new String[operations.length];
		List<Integer> arr = new ArrayList<>();

		String sum = String.join(" ", operations);
		String[] split = sum.split(" ");

		int count = 0;

		for (int i = 0; i < tq.length * 2;) {
			look[count] = split[i++];
			tq[count++] = Integer.parseInt(split[i++]);
		}

		for (int i = 0; i < look.length; i++) {
			if (look[i].equals("I")) {
				arr.add(tq[i]);
			} else {
				try {
					if (tq[i] == 1) {
						arr.remove(Collections.max(arr));
					} else {
						arr.remove(Collections.min(arr));
					}
				} catch (NoSuchElementException e) {
                    
				}
				
			}
		}try {
			answer[0] = Collections.max(arr);
			answer[1] = Collections.min(arr);
		} catch (NoSuchElementException e) {

		}
		return answer;
	}
}