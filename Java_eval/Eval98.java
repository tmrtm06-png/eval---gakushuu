import java.util.Scanner;

public class Eval98 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            double inputNum;

            // 1. 실수 입력 -> 2. 0.0 <= inputNum <= 1.0 범위 내 값이 아니면 반복 -> 3. 결과 출력
            // do-while 문으로 0.0 <= inputNum <= 1.0이 들어올 때까지 반복 입력받음
            do {

                inputNum = sc.nextDouble();
            } while (inputNum < 0.0 || inputNum > 1.0);

            // 결과 출력
            System.out.println("입력값: " + inputNum);
        }
    }
}