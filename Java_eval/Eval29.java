import java.util.Scanner;

public class Eval29 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int divTotal =0;
        // 1..N 중 N 을 나누어떨어지게 하는 값들의 합을 구해
        //       "약수 합: <합>" 출력.
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                divTotal += i;
            }
        }
        System.out.println("약수 합: " + divTotal);
        sc.close();
    }
}


// 피드백
// 1..√N 까지만 순회하여 약수 쌍을 동시에 더함 → O(√N) 최적화
        //         for (int i = 1; (long) i * i <= n; i++) {
        //     if (n % i == 0) {
        //         divTotal += i;
        //         if (i != n / i) {          // 완전제곱수일 때 중복 방지
        //             divTotal += n / i;
        //         }
        //     }
        // }