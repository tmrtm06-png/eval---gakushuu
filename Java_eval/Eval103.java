import java.util.Scanner;

public class Eval103 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            // 0. 총합 변수와 유효값 카운트 변수 선언
            int sum = 0, count = 0; 

            // 1. for 문으로 n번 반복하며 숫자를 입력받는다
            for (int i = 0; i < n; i++) {
                int currentNum = sc.nextInt();
                
                // 2. 현재 숫자가 1...100 범위 내면 sum에 현재값, count + 1 가산
                if (currentNum >= 1 && currentNum <= 100) {
                    count++;
                    sum += currentNum;
                }
            }
            
            // 3. 결과 출력 - count값이 0보다 큰 경우 평균(소수 둘째자리까지) 출력
            // 0인 경우 "유효값 없음" 출력
            if (count > 0) {
                double average = (double) sum / count;  // 자료형 double로 변환 필요함
                System.out.printf("평균: %.2f%n", average);
            } else {
                System.out.println("유효값 없음");
            }
        }
    }
}

// 피드백
// 유효 범위 경계값을 상수로 분리하여 의미 명확화
// private static final int MIN_VALID = 1;
// private static final int MAX_VALID = 100;