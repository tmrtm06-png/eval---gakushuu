import java.util.Scanner;

public class Eval89 {

    // 0. 월을 일수로 변환하기 위한 상수 선언
    private static final int MONTH_TO_DAY = 30;

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            // int y = sc.nextInt(); // 현재 계산에 사용되지 않음
            int m = sc.nextInt();
            int d = sc.nextInt();

            // 1. 입력받은 달과 일수의 총합 일수를 구한다 - (m - 1) * 30 + d
            int days = (m - 1) * MONTH_TO_DAY + d;

            // 2. 총 일수를 출력 - days + "일째"
            System.out.println(days + "일째");  
        }
    }
}