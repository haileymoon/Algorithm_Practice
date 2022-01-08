import java.util.*;

//우선 숫자가 같은 것들을 확인하고 개수를 확인
//0의 개수를 확인 -> 모르는 개수
//그럼 6개 - (0의 개수+맞는거 개수) = 틀린개수
//틀린 value를 알아야 함 (모르는 것들과 분리시켜야 나중에 모르는 것이 어떤값인지 알 수 있음)
//최고순위가 되려면 모르는 번호(0)가 남은 value랑 매치되어야 함
//최소순위가 되려면 모르는 번호가 win_nums와 겹치지 않는 value가 아무거나 들어가면 됨
//마지막으로 그 순위를 return 해야 함

class MyRawCodeLotto {
    public static void main(String[] args) {
        int[] lottos = {44, 1, 0, 0, 31, 25};
        int[] win_nums = {31, 10, 45, 1, 6, 19};
        int[] array = lotto(lottos,win_nums);
        for(int i=0; i<array.length; i++){
            System.out.println(array[i]);
        }
        
    }
    public static int[] lotto(int[] lottos, int[] win_nums) {
        int correct_count = 0;
        int array_size = lottos.length-1;

        ArrayList<Integer> lottos_list = new ArrayList<Integer>(array_size+1);
        ArrayList<Integer> win_nums_list = new ArrayList<Integer>(array_size+1);
        for (int i: lottos) lottos_list.add(i);
        for (int i: win_nums) win_nums_list.add(i);
        
        ArrayList<Integer> mismatch_value = new ArrayList<Integer>();
        ArrayList<Integer> mismatch_index = new ArrayList<Integer>();

        for(int i =0; i<=array_size; i++){
            if(win_nums_list.contains(lottos_list.get(i))){
                correct_count++;
            }
            else if(lottos_list.get(i) == 0){
                mismatch_value.add(win_nums_list.get(i));
                mismatch_index.add(i);
            }else {
                mismatch_value.add(win_nums_list.get(i));
            }
        }
        //최소순위
        Random randomGenerator = new Random();
        int randomInt = randomGenerator.nextInt(45) + 1;
        for (int i=0; i<mismatch_index.size();i++){
            if (randomInt != (int)mismatch_value.get(i)){
                lottos[(int)mismatch_index.get(i)] = randomInt;
            }
        }
        int lowest = rank(correct_count);
        //최고순위 - 모르는 번호가 win_nums와 겹치지 않는 value가 아무거나 나와야 함
        for (int i=0; i<mismatch_index.size();i++){
            lottos[(int)mismatch_index.get(i)] = (int)mismatch_value.get(i);
            correct_count++;
        }
        int highest = rank(correct_count);

        int[] answer = {highest, lowest};
        return answer;
    }
    public static int rank(int count){
        int rank_num = 0;
        switch(count){
            case 6: rank_num = 1;
                break;
            case 5: rank_num = 2;
                break;
            case 4: rank_num = 3;
                break;
            case 3: rank_num = 4;
                break;
            case 2: rank_num = 5;
                break;
            default: rank_num = 6;
                break;
        }
        return rank_num;
    }
}