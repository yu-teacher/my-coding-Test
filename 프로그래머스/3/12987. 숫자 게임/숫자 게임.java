import java.util.Arrays;
class Solution {
    public int solution(int[] A, int[] B){
        int answer = 0;
        int count = 0;
        Arrays.sort(A);
        Arrays.sort(B);
        
        for (int i = 0; i < B.length; i++) {
        		if(A[i-count] < B[i]) {
            		answer++;
            		continue;
            	}
            	count++;
		}
        return answer;
    }
}