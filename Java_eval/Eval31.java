import java.util.Scanner;

public class Eval31 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int oddSum = 0;  // 홀수 총합 변수 초기화
        int evenSum = 0;  // 짝수 총합 변수 초기화

        // for문으로 입력받은 1...n의 범위 내 홀수 총합과 짝수 총합을 구한다
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {
                evenSum += i;
            } else {
                oddSum += i;
            }
        }
        System.out.println("홀수 합: " + oddSum);
        System.out.println("짝수 합: " + evenSum);
        sc.close();
    }
}

// 피드백 
// 1~N 순회하며 홀수/짝수 분기 후 각각 누적
        // try (Scanner sc = new Scanner(System.in)) {} // try-with-resources로 자원 자동 해제