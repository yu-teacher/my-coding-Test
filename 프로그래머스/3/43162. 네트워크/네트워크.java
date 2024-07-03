class Solution {
    public void remove(int startnum ,int[][] arr) {
		for (int i = 0; i < arr.length; i++) {
			if(arr[startnum][i]==1) {
				arr[startnum][i]=0;
				remove(i, arr);
			}
		}
	}
	public int solution(int n, int[][] computers) {
		int count = 0;
		
		for (int i = 0; i < computers.length; i++) {
			if(computers[i][i]==0) continue;
			remove(i,computers);
			count++;
		}
		return count;
    }
}