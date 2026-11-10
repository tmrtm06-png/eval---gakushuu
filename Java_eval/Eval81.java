import java.util.Scanner;

public class Eval81 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int firstTerm = sc.nextInt();
            int ratio = sc.nextInt();
            int n = sc.nextInt();

            // StringBuilder로 효율화
            StringBuilder sb = new StringBuilder();

            // start를 term으로 두어 별도 관리 - type은 long으로 
            long term = firstTerm;

            // n번 반복하며 첫 항 firstTerm부터 ratio씩 곱해가는 반복문
            for (int i = 0; i < n; i++) {
                
                // 첫 숫자를 제외한 모든 숫자의 앞에 공백 추가
                if (i > 0) {
                    sb.append(" ");
                }

                // 등비수열 계산 후 sb에 추가
                sb.append(term);

                term *= ratio; // 다음 항으로 이동
            }
            
            // 결과 출력
            System.out.println(sb);
        }
    }
}