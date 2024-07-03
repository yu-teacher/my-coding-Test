import java.util.Arrays;
class Solution {
    public long solution(int n, int[] works) {
        long hardworks = 0;
        Arrays.sort(works);
        for (int i = 0; i < works.length; i++) {
			hardworks+=works[i];
		}
        hardworks-=n;
        if(hardworks<=0) {
        	return 0;
        }
        int temp = 0;
        int[] arr = new int[works.length];
        while (hardworks>0) {
        	for (int j = temp; j < arr.length; j++) {
        		arr[j]+=1;
        		hardworks-=1;
        		if(hardworks==0)break;
			}
        	if(arr[temp]==works[temp]) {
        		while (arr[temp] == works[temp]) {
					temp++;
				}
        	}
		}
        hardworks=0;
        for (int i = 0; i < arr.length; i++) {
        	hardworks+=arr[i]*arr[i];
		}
        return hardworks;
    }
}