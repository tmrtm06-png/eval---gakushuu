import java.util.Scanner;

public class Eval86 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            // 0. StringBuilder 작성
            StringBuilder sb = new StringBuilder();

            // 1. 2 * n - 1만큼 반복하는 반복문 작성
            for (int i = 1; i <= 2 * n - 1; i++) {

                // 2-1. 첫 숫자를 제외한 나머지 숫자를 공백 구분
                if (sb.length() > 0) {
                    sb.append(" ");
                }

                // 2-2. Math.min(i, 2*n - i)을 sb에 저장
                // - Math.min(i, 2*n - i) 해당 코드 안에서 1씩 증가하는 i만 sb에 저장됨 - 가장 작기 때문
                sb.append(Math.min(i, 2*n - i));
            }

            // 3. 결과 출력
            System.out.println(sb);
        }
    }
}

// 피드백
// 2-2. 주석 다듬기
// - i <= n 구간: i가 더 작아 i가 출력 (증가)
// - i > n 구간: 2*n-i가 더 작아 2*n-i가 출력 (감소)