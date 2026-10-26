import java.util.Scanner;

public class Eval57 {
    public static void main(String[] args) {
    try (Scanner sc = new Scanner(System.in)) {
        int n = sc.nextInt();
        
        // 1...n의 범위 내, n의 약수인 숫자만 공백 구분하여 한 줄로 출력
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                System.out.print(i + " ");
            }
        }
        System.out.println();
        }
    }
}


// 피드백
// import java.util.Scanner;
// import java.util.StringJoiner; ← 문자열을 특정 구분자와 함께 사용하여 결합할 때 사용되는 클래스

//             // 1...n의 범위 내, n의 약수인 숫자만 공백 구분하여 한 줄로 출력
//             StringJoiner joiner = new StringJoiner(" "); // 구분자만 삽입 → trailing space 없음
//             for (int i = 1; i <= n; i++) {
//                 if (n % i == 0) {
//                     joiner.add(String.valueOf(i));
//                 }
//             }
//             System.out.println(joiner); // 마지막 공백 없이 줄바꿈
//         }
//     }
// }