import java.util.Scanner;

public class Eval38 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int count = 0;  // 약수 count 변수 초기화

        // for 문으로 입력받은 정수 n이 1~n의 범위 내 숫자를 약수로 가지는 경우
        // count 변수 1씩 가산
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) {
                count++;
            }
        }
        System.out.println("약수 개수: " + count);
        sc.close();
    }
}



// 피드백
// √n까지만 순회하여 O(√N)으로 효율 개선
        // i와 n/i를 쌍으로 세되, 완전제곱수일 때는 1개만 카운트
        // for (int i = 1; (long) i * i <= n; i++) {
        //     if (n % i == 0) {
        //         count++;          // i 자체가 약수
        //         if (i != n / i) {
        //             count++;      // n/i 도 약수 (i ≠ n/i 일 때만)
        //         }
        //     }
        // }