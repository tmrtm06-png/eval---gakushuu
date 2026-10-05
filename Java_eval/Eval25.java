import java.util.Scanner;

public class Eval25 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sum = 0;
        // for 문으로 반복하며, i부터 n까지의 숫자 중 3의 배수인 경우 건너뛴다
        // 3의 배수가 아닌 경우 총 합계 변수에 가산
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0) {
                continue;
            } else {
                sum += i;
            }
        }
        // 요구 형식에 대응하여 총 합계 출력
        System.out.println("합계: " + sum);
        sc.close();  // - 자원 절약
    }
}


// // try-with-resources로 Scanner 자원을 자동 해제
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            int sum = 0;
            // for 문으로 반복하며, i부터 n까지의 숫자 중 3의 배수인 경우 건너뛴다
            // 3의 배수가 아닌 경우 총 합계 변수에 가산
            for (int i = 1; i <= n; i++) {
                if (i % 3 == 0) continue; // continue 후 else 불필요 — 이후 코드가 자동 스킵됨
                sum += i;
            }
            // 요구 형식에 대응하여 총 합계 출력
            System.out.println("합계: " + sum);
        }