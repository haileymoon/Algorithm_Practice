
public class Fourth_RevisedPlusMinus {
    public int solution(int[] absolutes, boolean[] signs) {
        int answer = 0;
        for (int count = 0; count<signs.length; count++){
            answer = absolutes[count] * (signs[count] ? 1:-1);
        }
        return answer;
    }
}
