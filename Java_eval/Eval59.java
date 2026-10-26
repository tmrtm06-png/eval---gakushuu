import java.util.Scanner;

public class Eval59 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
        int n = sc.nextInt();
        boolean isPrime = true; // 플래그 변수 설정 -> true인 경우 "소수" 출력

        // 2...n-1의 범위 내 값 중, i로 나눠떨어지는 값이 있는 경우 소수가 아님 
        // -> 플래그 변수 false로 변경 후 "소수 아님" 출력
        for (int i = 2; i < n; i++) {
            if (n % i == 0) {
                isPrime = false;
            }
        }
        if (isPrime) {
            System.out.println("소수");
        } else {
            System.out.println("소수 아님");
        }
    }
    }
}


// 피드백
// public class Main {

//     // 소수 판별 로직을 별도 메서드로 분리 -> 재사용성 및 가독성 향상
//     static boolean isPrime(int n) {
//         boolean flag = true; // 플래그 변수 설정 -> true인 경우 "소수"

//         // 2...n-1의 범위 내 값 중, i로 나눠떨어지는 값이 있는 경우 소수가 아님
//         // -> 플래그 변수 false로 변경 (break 없이 끝까지 순회)
//         for (int i = 2; i < n; i++) {
//             if (n % i == 0) {
//                 flag = false;
//             }
//         }
//         return flag;
//     }

//     public static void main(String[] args) {
//         try (Scanner sc = new Scanner(System.in)) {
//             int n = sc.nextInt();
//             System.out.println(isPrime(n) ? "소수" : "소수 아님");
//         }
//     }
// }