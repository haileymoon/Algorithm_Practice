public import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.LinkedList;

class Solution {
    String hand = "";
    int[] left_xy = {0,3};
    int[] right_xy = {2,3};
    int mid_x = 1;

    ArrayList<Integer> left_list = new ArrayList<Integer>(Arrays.asList(1,4,7));
    ArrayList<Integer> mid_list = new ArrayList<Integer>(Arrays.asList(2,5,8,0));
    ArrayList<Integer> right_list = new ArrayList<Integer>(Arrays.asList(3,6,9));

    List<String> answers = new LinkedList<String>();
    
    public String solution(int[] numbers, String hand) {
        this.hand = hand;
        for(int num: numbers){
            if (left_list.contains(num)){
                answers.add("L");
                this.left_xy[0] = 0;
                this.left_xy[1] = left_list.indexOf(num);
            }
            else if (right_list.contains(num)){
                answers.add("R");
                this.right_xy[0] = 2;
                this.right_xy[1] = right_list.indexOf(num);
            }
            else if (mid_list.contains(num)){
                String chosen_hand = choose_hand(num);
                if (chosen_hand.equals("right")){
                    answers.add("R");
                    this.right_xy[0] = mid_x;
                    this.right_xy[1] = mid_list.indexOf(num);
                }else if (chosen_hand.equals("left")) {
                    answers.add("L");
                    this.left_xy[0] = mid_x;
                    this.left_xy[1] = mid_list.indexOf(num);
                }
            }
        }
        
        return String.join("",answers);
    }
    public String choose_hand(int num){
        String chosen_hand = "";
        
        int left_y = Integer.valueOf(left_xy[1]);
		//#또는 *인 경우 y 좌표 설정        
		left_y = (left_y == -1) ? 3:left_y;
        
        int right_y = Integer.valueOf(right_xy[1]);
        right_y = (right_y == -1) ? 3:right_y;
        
        int[] left_index = {left_xy[0], left_y};
        int[] mid_index = {mid_x, Integer.valueOf(mid_list.indexOf(num))};
        int[] right_index = {right_xy[0], right_y};
        
        int left_mid_dist = find_distance(left_index, mid_index);
        int right_mid_dist = find_distance(right_index, mid_index);
        if (left_mid_dist < right_mid_dist){
            chosen_hand = "left";
        }
        else if (left_mid_dist == right_mid_dist){
            chosen_hand = this.hand;
        }
        else chosen_hand = "right";
        return chosen_hand;
    }
    public int find_distance(int[] a, int[] b){
        return Math.abs(a[0] - b[0])+ Math.abs(a[1]-b[1]);
    }
}