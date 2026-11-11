import java.util.Scanner;

public class Eval83 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            
            // 수도코드
            // 0. StringBuilder로 효율화 - 마지막에 한 번에 출력
            // 1. 1...n의 범위를 반복 순회
            // 2. 첫 숫자를 제외한 모든 숫자의 앞에 ", "를 붙인다
            // 3. 루프 종료 후 마침표를 한 번만 추가
           

            // StringBuilder 작성
            StringBuilder sb = new StringBuilder();

            // 입력받은 n의 범위 (1...n)내의 숫자 순회
            for (int i = 1; i <= n; i++) {

                // 첫 숫자를 제외한 모든 숫자 앞에 접두사
                if (i > 1) {
                    sb.append(", ");
                }

                sb.append(i);
                
                // 마지막 숫자인 경우 "."를 접미사로
                if (i == n) {
                    sb.append(".");
                }
            }

            // 결과 출력
            System.out.println(sb);
        }
    }
}

// 피드백
// 마침표를 루프 밖에서 한 번만 추가 → 조건 분기를 제거한다