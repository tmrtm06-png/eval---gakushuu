import java.util.Scanner;

public class Eval24 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        // while (true) 로 반복하며 정수를 입력받아
        // 변수 n에 저장 
        while (true) {
            int n = sc.nextInt();  // n에 유저가 입력한 정수를 저장
            
            // n의 값에 0이 입력된 경우 즉시 종료
            if (n == 0) {
                break;
            }
            // 종료되지 않은 경우는 sum += n
            sum += n;
        }
        // 반복 종료 후 총합을 출력 - "합계: " + 총합 값 형식
        System.out.println("합계: " + sum);
        sc.close();
    }
}