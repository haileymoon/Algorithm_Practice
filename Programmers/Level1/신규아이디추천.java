public class Solution {
    public String solution(String new_id) {
        //알파벳 말고 다른게 있어도 그걸 무시하고 대문자인것들만 속속들이 뽑아서 lowercase로 만듦
        new_id = new_id.toLowerCase(); 
        //정규식으로 표현
        new_id = new_id.replaceAll("[^a-z\\d-_.]","");
        //.이 두번 이상 반복된 경우 하나로 치환 -> ..으로 하니까 모든 문자로 인식해버림
				//escape문자 추가 필요
        new_id = new_id.replaceAll("\\.\\.+","\\."); 
        //처음이나 끝에 위치한다면 . 제거
        new_id = new_id.replaceAll("^(\\.)|(\\.)$","");
        if(new_id.equals("")){
            new_id = "a";
        }
        if(new_id.length()>=16){
            new_id = new_id.substring(0,15);
            new_id = new_id.replaceAll("(\\.)$","");
        }else if(new_id.length()<=2){
            while(new_id.length()!=3) {
                String add = new_id.substring(new_id.length()-1,new_id.length()).repeat(1);
                new_id = new_id+ add;
                }
        }
        return new_id;
    }
}