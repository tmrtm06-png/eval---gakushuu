import java.util.Scanner;

public class Eval80 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int start = sc.nextInt();
            int commonD = sc.nextInt();
            int n = sc.nextInt();

            // StringBuilder로 문자열 조합 후 마지막에 한 번 출력 - 효율화
            StringBuilder sb = new StringBuilder();

            // n번 순회하며 첫 항 start부터 공차 commonD씩 더해가는 반복문 작성
            for (int i = 0; i < n; i++) {
                 
                // 첫 숫자를 제외한 모든 나머지 숫자의 앞에 공백 추가
                if (i > 0) {
                    sb.append(" ");
                }
                sb.append(start + i * commonD);
            }
            
            // 결과 출력
            System.out.println(sb);
        }
    }
}