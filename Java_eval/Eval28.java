import java.util.Scanner;

public class Eval28 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int nkTotal = 0;
        // for 문으로 1..n 범위 내의 숫자 중, k의 배수의 합을 출력
        for (int i = 1; i <= n; i++) {
            if (i % k == 0) {
                nkTotal += i;
            }
        }
        System.out.println(k + "의 배수 합: " + nkTotal);
        sc.close();
    }
}

// 피드백
// 수학 공식으로 O(1) 계산: 1..n 중 k의 배수 개수 m = n/k, 합 = k * m * (m+1) / 2
        // int m = n / k;
        // int sumOfMultiples = k * m * (m + 1) / 2; // 등차수열 합 공식 활용