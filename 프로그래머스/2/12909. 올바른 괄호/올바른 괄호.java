class Solution {
    boolean solution(String s) {
		boolean answer = true;
		int count=0;
		char[] arr = new char[s.length()];
		for (int i = 0; i < s.length(); i++) {
			arr[i] = s.charAt(i);
		}
		for (int i = 0; i < s.length(); i++) {
			if(count==-1) {
				break;
			}
			if(arr[i]==41) {
				count--;
			}else if(arr[i]==40) {
				count++;
			}
		}
		answer = (count==0)? true:false;
		return answer;
	}
}