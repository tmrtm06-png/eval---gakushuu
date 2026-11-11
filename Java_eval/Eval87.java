import java.util.Scanner;

public class Eval87 {

    // 0. 시간과 분을 구할 때 사용하는 몫을 상수 선언
    public static final int REQ_HOUR = 3600;
    public static final int REQ_MIN = 60;

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int total = sc.nextInt();

            // 1. 입력받은 total을 REQ_HOUR로 나눠 시간을 구함
            // - 이후 나머지를 구한다
            int h = total / REQ_HOUR; 
            int remain = total % REQ_HOUR;

            // 2. remain을 REQ_MIN으로 나눠 분을 구한다
            // - 이후 초를 구한다 (remain을 REQ_MIN으로 나눈 나머지)
            int m = remain / REQ_MIN;
            int s = remain % REQ_MIN;

            // 3. 시, 분, 초를 요구 형식에 맞춰 한 줄로 출력한다
            System.out.println(h + "시간 " + m + "분 " + s + "초");
        }
    }
}

// 피드백
// 0. → private 으로 접근 제한자를 좁혀 캡슐화 강화
//  private static final int REQ_HOUR = 3600;
//  private static final int REQ_MIN = 60;

// 3. → printf 사용으로 출력 형식을 명확하게 표현
//  System.out.printf("%d시간 %d분 %d초%n", h, m, s);