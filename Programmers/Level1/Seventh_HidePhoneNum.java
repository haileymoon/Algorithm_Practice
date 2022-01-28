class Solution {
    public String solution(String phone_number) {
        String answer = "";
        int secret = 4;
        int secret_length = phone_number.length()-secret;
        answer = "*".repeat(secret_length)+phone_number.substring(secret_length,phone_number.length());
        return answer;
    }
}