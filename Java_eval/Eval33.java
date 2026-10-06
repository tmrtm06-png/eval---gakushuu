import java.util.Scanner;

public class Eval33 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
        int n = sc.nextInt();
        int posNumTotal = 0;
        
        // for 문으로 n만큼 반복하며 한 줄의 정수를 입력받는다
        // 정수가 음수인 경우 무시, 양수인 경우 양수 총합 변수에 가산
        for (int i = 0; i < n; i++) {
            int inputNum = sc.nextInt();
            if (inputNum > 0) {
            posNumTotal += inputNum;
            }
        }
        // 양식에 맞춰 양수의 총합을 출력
        System.out.println("양수 합: " + posNumTotal);
        }
    }
}

// 피드백
// Scanner sc = new Scanner(System.in); // 콘솔 입력이므로 try-with-resources 불필요
//         int n = sc.nextInt();
//         long posNumTotal = 0; // 큰 입력값 대비 long 사용