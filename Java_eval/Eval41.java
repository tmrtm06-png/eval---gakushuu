import java.util.Scanner;

public class Eval41 {
    
    // 합격 기준 점수 상수화
    public static final int PASS_SCORE = 60; 

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int passCounter = 0; // 합격자 수 카운터 초기화

        // for 문으로 n만큼 반복하며 정수를 입력받는다
        // 입력받은 점수가 합격 기준 이상인 경우 합격 카운터 가산 +1
        for (int i = 0; i < n; i++) {
            int inputNumber = sc.nextInt();
            if (inputNumber >= PASS_SCORE) {
                passCounter++;
  
            }
        }
        System.out.println("합격자 수: " + passCounter);
        sc.close();
    }
}