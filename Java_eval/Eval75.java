import java.util.Scanner;

public class Eval75 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            long n = sc.nextLong();

            // 자릿수 중 0 유무 판독을 위한 변수 초기화 - false로 초기화 후 0 발견 시 true로 갱신
            boolean hasZero = false; 

            while (n > 0) {
                long currentDigit = n % 10;
                n /= 10; // 다음 자릿수로 이동

                // 현재 자릿수에 0이 있는지 판별
                if (currentDigit == 0) {
                    hasZero = true;
                }
            }

            // 결과 출력 - 플래그 변수가 true인 경우 "있음", false인 경우 "없음" 출력
            if (hasZero) {
                System.out.println("있음");
            } else {
                System.out.println("없음");
            }
        }
    }
}


// 피드백
// 논리 OR 연산으로 플래그 갱신 — if문 없이 간결하게 표현
// hasZero = hasZero || (n % 10 == 0);
// n /= 10; // 다음 자릿수로 이동


// 결과 출력 - 플래그 변수가 true인 경우 "있음", false인 경우 "없음" 출력

// System.out.println(hasZero ? "있음" : "없음");

// 상기 삼항연산자 코드 요소 분해
// hasZero: 조건
// ?: 조건 판단 구분자
// "있음": true인 경우의 값
// "없음": false인 경우의 값 