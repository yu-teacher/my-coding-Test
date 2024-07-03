import java.util.Arrays;
import java.util.Comparator;
class Solution {
    public int solution(int[][] routes) 
	{
        int answer = 1;
        Arrays.sort(routes, new Comparator<int[]>() {

			@Override
			public int compare(int[] o1, int[] o2) {
				if(o1[0] == o2[0]) {
					return o2[1]-o1[1];
				}else {
					return o1[0]-o2[0];
				}
			}
		});
        int startNum = routes[0][0];
        int endNum = routes[0][1];
        
        for (int i = 0; i < routes.length; i++) {
        	if (startNum < routes[i][0]) {
				startNum = routes[i][0];
			}
        	if (endNum > routes[i][1]) {
				endNum = routes[i][1];
			}
        	if (endNum < startNum) {
				answer++;
				try {
					startNum = routes[i][0];
					endNum = routes[i][1];
				} catch (Exception e) {
					break;
				}
			}
		}
        return answer;
    }
}