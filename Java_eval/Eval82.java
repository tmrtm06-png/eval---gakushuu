import java.util.Scanner;

public class Eval82 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            // StringBuilder로 효율화
            StringBuilder sb = new StringBuilder();

            // 입력받은 n만큼 반복
            for (int i = 1; i <= n; i++) {

                // 첫 숫자를 제외한 모든 숫자의 앞에 공백 추가
                if (sb.length() > 0) {
                    sb.append(' ');
                }

                // i가 짝수인 경우 -, 홀수인 경우 +를 붙임
                if (i % 2 == 0) {
                    sb.append("-" + i);
                } else {
                    sb.append("+" + i);
                }
            }

            // 결과 출력
            System.out.println(sb);
        }
    }
}


// 피드백
//// 삼항 연산자로 부호를 한 줄에 결정 — if-else 분기 제거
// String sign = (i % 2 == 0) ? "-" : "+";
// sb.append(sign).append(i); // 체이닝으로 임시 String 객체 생성 없이 추가