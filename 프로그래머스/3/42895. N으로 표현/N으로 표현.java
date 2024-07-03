import java.util.ArrayList;
class Solution {
    public int solution(int N, int number) {
		ArrayList<Integer>[] nf = new ArrayList[9];
		int num = N;
		for (int count = 1; count < 9; count++) {
			if (num == number)
				return count;
			nf[count] = new ArrayList<Integer>();
			nf[count].add(num);
			num = num * 10 + N;
			for (int a = 1; a < count; a++) {
				int b = count - a;

				for (Integer k : nf[a]) {
					for (Integer t : nf[b]) {
						if (k + t == number)
							return count;
						nf[count].add(k + t);
						if (k - t == number)
							return count;
						nf[count].add(k - t);
						if (k * t == number)
							return count;
						nf[count].add(k * t);
						if (t != 0) {
							if (k / t == number)
								return count;
							nf[count].add(k / t);
						}
					}
				}
			}
		}
		return -1;
	}
}