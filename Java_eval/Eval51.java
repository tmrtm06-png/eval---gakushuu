import java.util.Scanner;

public class Eval51 {
    public static void main(String[] args) {

        // 첫 입력값을 best의 초기값으로 설정 -> 반복하며 나머지의 절댓값을 비교 -> 결과 출력
        try (Scanner sc = new Scanner(System.in)) {
        int n = sc.nextInt();

        // 첫 입력값을 best의 초기값으로 설정
        int best = sc.nextInt();

        // 초기값을 입력받았으므로, (n - 1)만큼 반복하며 숫자를 입력받는다
        for (int i = 1; i < n; i++) {
            int currentNum = sc.nextInt();
            // 입력값의 절댓값이 best의 절댓값보다 작은 경우에만 변수 갱신
            // - 동률이 있는 경우 먼저 나온 값이 정답 (등호 제외)
            if (Math.abs(currentNum) < Math.abs(best)){
                best = currentNum;
            }
       }
       System.out.println("0에 가장 가까운 값: " + best);
       }
    }
}


// 피드백
// - 입력값의 범위가 int이므로 long 타입 불필요
// best의 절댓값을 별도의 변수로 관리하여 불필요한 계산 방지 -> int bestAbs = Math.abs(best);
// current도 통일하여 별도의 변수 작성 -> int currentAbs = Math.abs(currentNum);
// 해당 방법으로 작성 시, bestAbs = currentAbs; 와 같이 best 갱신 시 bestAbs도 함께 갱신해야 한다