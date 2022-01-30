import java.util.ArrayList;
import java.util.List;

class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        // n/2보다 다른게 많으면 n/2가 최대
        // 다른게 적으면 n/2가 채워질때까지 for문 돌리고 count 해줘야겠다
        int pick_number = nums.length/2;
        int count = 0;
        List<Integer> num_list = new ArrayList<Integer>();
        for(int num : nums){
            if (pick_number == num_list.size()){
                answer = num_list.size();
                break;                
            }else if(num_list.contains(num)){
                continue;                
            }else{
                num_list.add(Integer.valueOf(num));
            }
        }
        answer = num_list.size();
        return answer;
    }
}