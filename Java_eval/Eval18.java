import java.util.Scanner;

public class Eval18 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // while 문 사용
        // n 이하의 값들 중, 2의 거듭제곱을 공백 구분하여 한 줄로 출력
        // - 초기값 1부터 시작
        int start = 1;

        while (start <= n) {
            System.out.print(start + " ");
            start *= 2;
        }
        sc.close();
    }
}

// 피드백

        // while 문 사용
        // n 이하의 값들 중, 2의 거듭제곱을 공백 구분하여 한 줄로 출력
        // - 초기값 1부터 시작
//         int current = 1; // 'start' → 'current': 현재 출력 중인 2의 거듭제곱 값임을 명확히 표현
//         StringBuilder sb = new StringBuilder(); // trailing 공백 없이 출력하기 위해 사용

//         while (current <= n) {
//             if (sb.length() > 0) sb.append(' '); // 첫 번째 값 앞에는 공백을 붙이지 않음
//             sb.append(current);
//             current *= 2;
//         }

//         System.out.println(sb);
//         sc.close();
//     }
// }