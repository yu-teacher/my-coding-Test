import java.util.*;
class Solution {
    public long[] solution(long k, long[] room_number) {
		Map<Long, Long> visitTimes = new HashMap<>();
		long[] answer = new long[room_number.length];
		for (int i = 0; i < room_number.length; i++) {

			Long count = visitTimes.get(room_number[i]);
			if (count == null) {
				visitTimes.put(room_number[i], room_number[i]);
				answer[i] = room_number[i];
				continue;
			}
			
			Set<Long> tempStay = new HashSet<>();
			
			Long j = visitTimes.get(room_number[i]);
			
			while (true) {
				if (visitTimes.get(j) == null) {
					tempStay.add(j);
					for (Long visit : tempStay) {
						visitTimes.put(visit, j);
					}
					answer[i] = j;
					break;
				} 
				else {
					tempStay.add(j);
					j = visitTimes.get(j);
				}
				j++;
			}
		}
		return answer;
	}
}