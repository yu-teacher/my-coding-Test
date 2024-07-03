class Solution {
    public int solution(int sticker[]) {
        
        int leng = sticker.length;
        
        if(leng == 1)
            return sticker[0];
        
        
        int[] type1 = new int[leng];
        int[] type2 = new int[leng];
        
        type1[0] = type1[1] = sticker[0];
        type2[1] = sticker[1];
        
        for(int i = 2; i < leng; i++){
            type1[i] = Math.max(type1[i-1] , sticker[i] + type1[i-2]);
            type2[i] = Math.max(type2[i-1] , sticker[i] + type2[i-2]);
        }
        
        return Math.max(type1[leng-2], type2[leng-1]);
    }
}