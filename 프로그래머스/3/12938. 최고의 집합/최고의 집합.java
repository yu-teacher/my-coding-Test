import java.util.*;
class Solution {
    public int[] solution(int n, int s) {
		int[] arr1 = new int[n];
		if (n > s) {
			int[] arr2 = new int[1];
			arr2[0]=-1;
			return arr2;
		}
		int num = s / n;
		for (int i = 0; i < n; i++) {
			arr1[i] = num;
		}
		num = s % n;
		int i = 0;
		while (num > 0) {
			arr1[i] += 1;
			i++;
			num--;
		}
		Arrays.sort(arr1);
		return arr1;
	}
}