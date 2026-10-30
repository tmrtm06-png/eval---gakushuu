import java.util.Scanner;

public class Eval67 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int copiedN = n;

            // 자릿수 최솟값 변수 초기화 - 범위가 0...9 이므로 9로 초기화한다
            int min = 9;

            // 복사본 copiedN이 0보다 클 때까지만 반복 - while문
            while (copiedN > 0) {
                int digit = copiedN % 10; // copiedN을 10으로 나눈 나머지를 변수에 저장
     
                // 자릿수가 min보다 작은 경우 변수 갱신
                if (min > digit) {
                    min = digit;
                }

                // 이후 copiedN도 10으로 나눠 갱신
                copiedN /= 10;
            }

            // 결과 출력
            System.out.println("자릿수 최솟값: " + min);
        }
    }
}


// 피드백
// Math.min 으로 if 분기 없이 최솟값 갱신
// min = Math.min(min, digit);