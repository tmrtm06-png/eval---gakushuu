import java.util.Scanner;

public class Eval54 {

    // 자릿수 변수를 상수 선언
    public static final int DIGIT_BASE = 10;

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {

            int n = sc.nextInt();
            int maxDigit = 0; // 자릿수 판별 변수 초기화
            
            // n이 0보다 클 때까지 반복 - 양의 정수 조건에 부합
            // - 현재 자릿수의 값을 구한 후 변수에 저장 | 반복할 때마다 n을 DIGIT_BASE로 나누며 갱신
            while (n > 0) {
                int currentDigitNum = n % DIGIT_BASE;
                n /= DIGIT_BASE;

                // 현재 자릿수의 값이 최댓값 판별 변수보다 큰 경우 변수 갱신
                if (currentDigitNum > maxDigit) {
                    maxDigit = currentDigitNum;
                }
            }
            // 결과 출력
            System.out.println("자릿수 최댓값: " + maxDigit);
        }
    }
}