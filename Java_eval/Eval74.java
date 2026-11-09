import java.util.Scanner;

public class Eval74 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            long n = sc.nextLong();

            // 각 자릿수의 최댓값・최솟값을 구하는 변수를 초기화 
            // - 자릿수의 범위는 0...9이므로 int
            int digitMax = 0;
            int digitMin = 9;

            while (n > 0) {
                int currentDigit = (int) (n % 10); // long 타입인 n을 int로 추출

                // 현재 자릿수의 값과 최댓값・최솟값 변수를 비교 후, 변수 갱신
                if (currentDigit > digitMax) {
                    digitMax = currentDigit;
                }

                if (currentDigit < digitMin) {
                    digitMin = currentDigit;
                }

                n /= 10; // 다음 자리로 이동
            }

            // 결과 출력
            System.out.println("범위: " + (digitMax - digitMin));
        }
    }
}