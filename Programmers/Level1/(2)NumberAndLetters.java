import java.util.Map;
import java.util.HashMap;

class NumberAndLetters {
    public int numberAndLetters(String s) {
        Map<String, Integer> numbermap = new HashMap<>();
        numbermap.put("zero",0);
        numbermap.put("one",1);
        numbermap.put("two",2);
        numbermap.put("three",3);
        numbermap.put("four",4);
        numbermap.put("five",5);
        numbermap.put("six",6);
        numbermap.put("seven",7);
        numbermap.put("eight",8);
        numbermap.put("nine",9);
        
        for(String key: numbermap.keySet()){
            String keyword = key.toString();
            if (s.contains(keyword)){
                String value = numbermap.get(key).toString();
                s = s.replace(keyword,value);
            }
        }
        int answer = Integer.parseInt(s);
        return answer;
    }
}