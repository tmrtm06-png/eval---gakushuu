import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            int max = Integer.MIN_VALUE; // 가장 작은 값으로 최대값 변수 초기화
            int maxIndex = 0; // 최대값의 인덱스 추적

            // n번 반복하며 숫자를 입력받는다
            // 인덱스는 (1-based)이므로, i는 1부터 시작
            for (int i = 1; i <= n; i++) {
                int currentValue = sc.nextInt();

                // 입력받은 숫자가 max보다 큰 경우 max변수를 갱신
                // 최대 인덱스 변수도 함께 갱신 - (현재 반복 횟수 i = 인덱스)
                if (currentValue > max) { // 가독성을 위해 currentValue를 왼쪽에 배치
                    max = currentValue;
                    maxIndex = i;
                }
            }

            // 결과 출력
            System.out.println("최댓값의 위치: " + maxIndex);
        }
    }
}