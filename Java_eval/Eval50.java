import java.util.Scanner;

public class Eval50 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
        int n = sc.nextInt();
        int best = sc.nextInt(); // 첫 숫자를 best의 초기값으로 설정

        // 첫 숫자를 입력받았으므로, (n-1)만큼 반복하며 숫자를 입력받는다
        for (int i = 1; i < n; i++) {
            int currentNum = sc.nextInt();
            // 입력받은 숫자의 절댓값이 best의 절댓값보다 큰 경우에만 best 갱신
            if (Math.abs(currentNum) > Math.abs(best)) {
                best = currentNum;
            }
        }

        // 결과 출력
        System.out.println("절댓값 최대의 값: " + best);
        }
    }
}

// 피드백
// 알고리즘의 전체 흐름을 주석으로 남김
// 입력값이 int 범위를 초과할 경우를 대비하여 best의 타입을 int -> long으로 변경