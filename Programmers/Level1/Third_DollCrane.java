import java.util.Stack;

public class DollCrane {
  public int solution(int[][] board, int[] moves) {
    int answer = 0;

    Stack<Integer> stack = new Stack<>();

    for (int move : moves) {
      for (int row = 0; row < board.length; row++) {
          int value = board[row][move - 1];
        if (value != 0) {
            if(stack.empty()) stack.push(value);
            else if (stack.peek() == value) {
                stack.pop();
                answer += 2;
            }else stack.push(value);
          board[row][move - 1] = 0;
          break;
        }
      }
    }
    return answer;
  }
}