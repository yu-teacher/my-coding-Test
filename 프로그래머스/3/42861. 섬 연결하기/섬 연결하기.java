import java.util.*;
class Solution {
    public int solution(int n, int[][] costs) {
        int answer = 0;
        
        Arrays.sort(costs, Comparator.comparingInt((int[] o) -> o[2]));
        
        boolean[] dp = new boolean[n];
        
        answer += costs[0][2];
        dp[costs[0][0]] = true;
        dp[costs[0][1]] = true;
        
        while(true){
            for(int j = 1; j < costs.length; j++){
                if((dp[costs[j][0]] == true)&&(dp[costs[j][1]]) == true){
                    continue;
                }else if((dp[costs[j][0]] == false)&&(dp[costs[j][1]]) == false){
                    continue;
                }else{
                    dp[costs[j][0]] = true;
                    dp[costs[j][1]] = true;
                    answer += costs[j][2];
                    break;
                }
            }
            
            boolean allTrue = true;
            
            for (boolean element : dp) {
                if (!element) {
                    allTrue = false;
                    break;
                }
            }
            
            if (allTrue) return answer;
        }
    }
}