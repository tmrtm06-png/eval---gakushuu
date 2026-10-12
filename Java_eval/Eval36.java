import java.util.Scanner;

public class Eval36 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // for 문으로 1~n의 범위 내의 숫자가 짝수인지 홀수인지 판별
        // 짝수인 경우 (result -= i) | 홀수인 경우 (result += i)
        int result = 0; 
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) {  // 짝수이면 result -= i 누적
                result -= i;
            } else {
                result += i;  // 홀수이면 result += i 누적
            }
        }
        // 결과 출력
        System.out.println("결과: " + result);
        sc.close();
    }
}