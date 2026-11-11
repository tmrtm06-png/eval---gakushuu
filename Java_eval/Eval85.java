import java.util.Scanner;

public class Eval85 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            // 0. StringBuilder 초기화 (용량 예약)
            StringBuilder sb = new StringBuilder(n);

            // 1. 입력받은 n만큼 반복
            for (int i = 1; i <= n; i++) {

                // 2-1. 첫 숫자의 앞에는 공백 X
                if (sb.length() > 0) {
                    sb.append(" ");
                }

                // 2-2. 범위 내 숫자 중 자연수의 제곱값이 n의 이하인 제곱값만 
                // 공백 구분하여 sb에 저장
                if (i * i <= n) {
                    sb.append(i * i);
                }
            }

            // 3. sb 출력
            System.out.println(sb);
        }
    }
}

// 피드백
// 반복문의 조건식에서 i * i <= n인 경우만 순회
// → 2-2.의 if문 불필요, 그대로 제곱값만을 sb에 저장