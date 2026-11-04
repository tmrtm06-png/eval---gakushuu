import java.util.Scanner;

public class Eval72 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            // 자릿수의 제곱의 합을 구하는 변수 - 자릿수는 0...9의 범위 내므로 타입은 int로
            int digitSum = 0;

            // while문으로 n을 각 자릿수로 분해한다
            // - 이후 상단의 변수에 더함
            while (n > 0) {
                int currentDigit = n % 10;
                digitSum += currentDigit * currentDigit;
                n /= 10;  // 입력받은 값 n을 갱신
            }
            
            // 결과 출력
            System.out.println("제곱합: " + digitSum);
        }
    }
}