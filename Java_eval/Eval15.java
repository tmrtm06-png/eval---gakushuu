import java.util.Scanner;

// 직접 작성한 코드
// public class Eval15 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int n = sc.nextInt();
//         // for 로 1..N 의 짝수 합을 구해 "짝수 합: <합계>" 형식으로 출력.

//         // 총합을 구하기 위한 변수를 초기화
//         int total = 0;
//         // 정수 num을 정의, 입력받은 정수 n의 범위만큼 포함하도록 조건식 작성 후
//         // 각 숫자를 더하는 식 작성
//         for (int num = 1; num <= n; num++) {
//             // 1에서 시작하는 정수 num이 짝수일 경우만 총합 변수에 더함
//             if (num % 2 == 0) {
//                 total += num;
//             }
//         }
//         // 루프 바깥에서 결과 출력
//         System.out.println("짝수 합: " + total);

//         // 자원 반환
//         sc.close();
//     }
// }


// 피드백 받은 코드
public class Eval15 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // for 로 1..N 의 짝수 합을 구해 "짝수 합: <합계>" 형식으로 출력.

        // 총합을 구하기 위한 변수를 초기화
        int total = 0;

        // num을 2부터 시작해 2씩 증가 → 짝수만 순회하므로 % 연산 불필요
        for (int num = 2; num <= n; num += 2) {
            total += num;
        }

        // 루프 바깥에서 결과 출력
        System.out.println("짝수 합: " + total);

        sc.close(); // 자원 반환
    }
}