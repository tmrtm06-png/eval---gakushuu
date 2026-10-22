import java.util.Scanner;

public class Eval52 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
        int n = sc.nextInt();
        // max와 second 변수를 초기화 -> n만큼 반복하며 숫자를 입력받는다 -> 숫자의 크기를 비교 후 변수 갱신 -> 결과 출력
        int max = Integer.MIN_VALUE;
        int second = 0; 
        
        // n만큼 반복하며 숫자를 정수를 입력받는다
        for (int i = 0; i < n; i++) {
            int currentNum = sc.nextInt();
            
            // 현재 숫자가 max보다 큰 경우
            // - second 변수를 max로 갱신, max 변수를 현재 숫자로 갱신한다
            if (currentNum > max) {
                second = max;
                max = currentNum;

              // 현재 숫자가 second보다 큰 경우
              // - second를 현재 숫자로 갱신
            } else if (currentNum > second) {
                second = currentNum;
            }
        }
        System.out.println("두 번째로 큰 값: " + second);
        }
    }
}


// 피드백
// int second = 0; 의 할당값을 Integer.MIN_VALUE로 초기화