import java.util.Scanner;
import java.util.StringJoiner;

public class Eval58 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
        int n = sc.nextInt();
        int k = sc.nextInt();

        // 1...n의 범위 내 숫자 중, k의 배수만 공백 구분하여 한 줄로 출력
        StringJoiner joiner = new StringJoiner(" "); // 구분자만 삽입하여 trailng space 없애기
        for (int i = 1; i <= n; i++) {
            if (i % k == 0) {
                joiner.add(String.valueOf(i));
            }
            }
            System.out.println(joiner); // 공백 없이 줄바꿈
        }
    }
}

// 피드백
// k씩 건너뛰며 배수만 직접 열거 → 나머지 연산 불필요
//  for (int i = k; i <= n; i += k) {
//     joiner.add(String.valueOf(i));
// }