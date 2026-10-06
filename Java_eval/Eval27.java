import java.util.Scanner;

public class Eval27 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        // a부터 b까지의 범위 내 숫자를 모두 더한 값을 출력
        int sum = 0;
        for (int i = a; i <= b; i++) {
            sum += i;
        }
        System.out.println("합계: " + sum);
        sc.close();
    }
}

// 피드백
        // Scanner scanner = new Scanner(System.in); // sc → scanner: 역할이 명확한 변수명
        // int a = scanner.nextInt();
        // int b = scanner.nextInt();

        // a부터 b까지의 범위 내 숫자를 모두 더한 값을 출력
        // 가우스 합산 공식으로 O(1) 계산: (a+b) * 항수 / 2
        // long totalSum = (long)(a + b) * (b - a + 1) / 2; // int 오버플로우 방지를 위해 long 사용

        // System.out.println("합계: " + totalSum);
        // scanner.close();