import java.util.Scanner;

public class Eval73 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            // 짝수 카운트 변수 초기화
            int count = 0;

            // while문으로 자릿수 분해
            while (n > 0) {
                int currentDigit = n % 10;

                // 각 자릿수의 값이 짝수인 경우 카운트 변수에 1씩 가산
                if (currentDigit % 2 == 0) {
                    count++;
                }

                // 다음 자리로 이동
                n /= 10;
            }

            // 결과 출력
            System.out.println("짝수 자리 개수: " + count);
        }
    }
}

// 피드백
// currentDigit 변수 없이 인라인으로 처리해 코드 간결화
//               if ((n % 10) % 2 == 0)