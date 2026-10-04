import java.util.Scanner;

public class Eval23 {
    public static void main(String[] args) {
        int numTotal = 0;
        int k = 0;

        // for 문으로 i의 값을 증가시키며, 내부에서 총합값 변수에 i를 가산
        for (int inputNum = 1; ; inputNum++) {
            numTotal += inputNum;
            // 총합 변수가 100을 넘어갈 때의 최초의 숫자를 k에 갱신, 이후 즉시 종료
            if (numTotal > 100) {
            k = inputNum;
            break;
            }
        }
        // 반복문 바깥에서 요구 양식대로 k와 당시의 총합을 두 줄로 출력
        System.out.println("1 + 2 + ... + k 가 100을 넘는 최초의 k = " + k);
        System.out.println("(그때의 합 = " + numTotal + ")");
    }
}


// 피드백
// int inputNum; // k 역할을 겸하도록 루프 바깥에 선언 (별도 k 변수 제거)

        // for 문으로 i의 값을 증가시키며, 내부에서 총합값 변수에 i를 가산
        // for (inputNum = 1; ; inputNum++) {
            // numTotal += inputNum;
            // 총합 변수가 100을 넘어갈 때 즉시 종료
            // if (numTotal > 100) {