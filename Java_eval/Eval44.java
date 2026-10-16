import java.util.Scanner;

public class Eval44 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int oddCount = 0; // 홀수 카운터 변수 초기화

        // 입력받은 반복문 범위 n만큼 숫자를 입력받는다
        // 입력받은 숫자가 홀수인 경우 홀수 카운터 +1 증가
        for (int i = 0; i < n; i++) {
            int num = sc.nextInt();
            if (num % 2 != 0) {
                oddCount++;
            }
        }
        System.out.println("홀수 개수: " + oddCount);
        sc.close();
    }
}


// 피드백
// 자바의 %연산이 음수에서도 작동하는 이유 주석 작성
// Java의 % 연산은 음수에서도 부호가 피제수를 따르므로 
// -3 % 2 = -1 != 0 → 올바르게 홀수 판별됨