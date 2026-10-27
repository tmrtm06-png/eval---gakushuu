import java.util.Scanner;

public class Eval60 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
        int n = sc.nextInt();
        int divTotal = 0;

        // 1..n-1의 범위 내의 숫자가, n의 약수인 경우 총합 변수에 가산
        for (int i = 1; i < n; i++) {
            if (n % i == 0) {
                divTotal += i;
            }
        }
        // 약수의 총합이 n과 같은 경우 "완전수" 완전수가 아닌 경우 "완전수 아님" 출력
        if (divTotal == n) {
            System.out.print("완전수");
        } else {
            System.out.print("완전수 아님");
        }
        }
    }
}


// 피드백
// 완전수 판별식을 별도의 메서드로 분리한다 
    // 완전수 판정 로직을 별도 메서드로 분리 → main 간결화 및 재사용성 향상
//    static boolean isPerfect(int n) {
//        if (n < 2) return false; // n==1 등 특수 케이스 명시적 처리
//        int divTotal = 0;

        // √n까지만 순회하여 약수 쌍(i, n/i)을 함께 합산 → O(√N)
//        for (int i = 1; (long) i * i <= n; i++) {
//            if (n % i == 0) {
//                divTotal += i; // 작은 약수 합산
//                if (i != 1 && i != n / i) {
//                    divTotal += n / i; // 대응하는 큰 약수 합산 (n 자체 제외)
//                 }
//             }
//         }
        // 약수의 총합이 n과 같은 경우 완전수
//        return divTotal == n;
//    }

//     public static void main(String[] args) {
//         try (Scanner sc = new Scanner(System.in)) {
//             int n = sc.nextInt();
//            System.out.print(isPerfect(n) ? "완전수" : "완전수 아님");
//         }
//     }