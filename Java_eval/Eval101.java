import java.util.Scanner;

public class Eval101 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {

            // 0. 직전 변수와 연속 카운트 변수 선언 및 초기화
            int prev = Integer.MIN_VALUE;
            int streak = 0;

            // 1. while문으로 같은 숫자가 연속 세 번 입력됐을 시 종료
            while (streak < 3) {
                
                // 2. 현재 숫자를 입력받는다
                int currentNum = sc.nextInt();
                
                // 3. 현재 숫자가 직전 숫자와 같은 경우 연속 변수 + 1 가산
                if (currentNum == prev) {
                    streak++;

                // 3-1. 아닌 경우 연속 변수 1로 초기화, 직전 숫자를 현 숫자로 갱신 
                } else {
                    streak = 1;
                    prev = currentNum;
                }
            }
            
            // 4. 결과 출력
            System.out.println("종료");
        }
    }
}

// 피드백
// 세 번 연속되기 전에 종료되는 경우 고려
// while문 조건에 hasNextInt 조건 추가
// → while (streak < 3 && sc.hasNextInt())