import java.util.Map.Entry;
import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Arrays;

class Solution {
    public Object[] solution(String[] id_list, String[] report, int k) {
        int[] answer = {};
        // report에 있는 신고 한 사람, 신고 당한 사람 나눠
        // id와 횟수용 해시테이블
        // k보다 크면 신고한 id를 신고당한 id와 해시테이블에 저장
        // 만약 k 보다 작거나 x해시테이블에 id가 신고한 id가 없으면 0넣어주기
        HashMap<String, String> case_per_id = new HashMap<>();
        HashMap<String, Integer> id_blocked = new LinkedHashMap<>();
        
        String[] report_case_array = Arrays.stream(report).distinct().toArray(String[]::new);

        for (String report_case : report_case_array){
            String[] split_report = report_case.split(" ");
            
            if(case_per_id.isEmpty()||!case_per_id.containsKey(split_report[1])){
                case_per_id.put(split_report[1], split_report[0]);   
            }else{
                case_per_id.replace(split_report[1],case_per_id.get(split_report[1])+" "+split_report[0]);
            }
        }
        for (String id : id_list){
            id_blocked.put(id,0);
        }
        for (String key : case_per_id.keySet()){
            String[] array = case_per_id.get(key).split(" ");
            if(array.length>=k){
                for (String blocker : array){
                    if (id_blocked.get(blocker)==0){
                        id_blocked.put(blocker, 1);
                    }else{
                        id_blocked.replace(blocker, id_blocked.get(blocker)+1);
                    }      
                }
            }
        }
        
        return id_blocked.values().toArray();
    }
}