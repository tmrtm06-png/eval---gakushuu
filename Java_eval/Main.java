import java.util.Scanner;

public class Main {

    // 0. 입력받은 시간과 분을 총 초수로 변환하기 위한 상수 선언
    private static final int TOTAL_HR_CONVERT = 3600;
    private static final int TOTAL_MIN_CONVERT = 60;
    
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int h = sc.nextInt();
            int m = sc.nextInt();
            int s = sc.nextInt();
            
            // 1. 입력받은 시, 분을 각 상수로 곱한 후, 초를 더하여 총합 변수에 저장
            int total = h * TOTAL_HR_CONVERT + m * TOTAL_MIN_CONVERT + s;
            
            // 2. 결과 출력
            System.out.println("총 " + total + "초");
            
        }
    }
}

// 피드백
// 상수명에 단위 관계를 명시하여 가독성 향상
// TOTAL_HR_CONVERT → SECONDS_PER_HOUR
// TOTAL_MIN_CONVERT → SECONDS_PER_MINUTE