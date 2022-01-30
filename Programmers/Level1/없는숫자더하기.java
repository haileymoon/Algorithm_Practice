import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        
        List <Integer> num_list = new ArrayList<Integer>();
        for(int num : numbers){
            num_list.add(num);
        }
        int[] full_num = {0,1,2,3,4,5,6,7,8,9};
        //numbers가 contain하고 있지 않는 fullnum의 숫자
        for(int num : full_num){
            if(!num_list.contains(num)){
                answer+= num;
            }
        }
        return answer;
    }
}