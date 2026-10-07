import java.util.Scanner;

public class Eval35 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int scoreSum = 0;  // 점수 총합 변수 초기화
        
        // for 문으로 반복하며 n번만큼 정수 점수를 입력받는다
        // - 점수 평균(총합 / n) 을 소수 둘째자리까지 구한 후 출력
        for (int i = 0; i < n; i++) {
            int inputScore = sc.nextInt();
            scoreSum += inputScore;
        }
        double avg = (double) scoreSum / n;
        System.out.printf("평균: %.2f", avg);
        sc.close();
    }
}



// 피드백
// long scoreSum = 0;  // 점수 총합 변수 초기화 (int 오버플로우 방지를 위해 long 사용)
// System.out.printf("평균: %.2f%n", avg);  // %n 으로 줄바꿈 명시

// n의 입력이 0인 경우를 대비한 방어 코드 작성
// // n이 0 이하이면 평균 계산 불가 — 방어 조건 추가
//         if (n <= 0) {
//             System.out.println("입력 오류: N은 1 이상이어야 합니다.");
//             sc.close();
//             return;
//         }