import java.util.Scanner;

public class Eval34 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long squareTotal = 0;  // 범위 내 숫자의 제곱 합 변수 초기화 - 큰 입력 대비하여 타입 long으로
        // for 로 i*i 누적해 "제곱합: <합>" 출력.
        for (int i = 1; i <= n; i++) {
            squareTotal += Math.pow(i, 2);  // 자바에서 제곱 연산자는 Math.pow(base, exp)가 제공된다
        }
        System.out.println("제곱합: " + squareTotal);
        sc.close();
    }
}


// 피드백
// quareTotal += (long) i * i;  // Math.pow 대신 정수 곱셈 사용 → 부동소수점 오차 방지