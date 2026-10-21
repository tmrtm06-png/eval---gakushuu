import java.util.Scanner;

public class Eval49 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        // 최솟값, 최댓값을 구하는 두 변수를 초기화
        int maxNum = Integer.MIN_VALUE;
        int minNum = Integer.MAX_VALUE;

        // 입력받은 n만큼 반복하며 숫자를 입력받는다
        for (int i = 0; i < n; i++) {
            int currentNum = sc.nextInt();
            // 현재 값이 최댓값 변수보다 큰 경우 변수 갱신
            if (currentNum > maxNum) {
                maxNum = currentNum;
            }
            // 현재 값이 최솟값 변수보다 작은 경우 변수 갱신
            if (currentNum < minNum) {
                minNum = currentNum;
            }
        }
        // 결과 출력
        System.out.println("최댓값: " + maxNum);
        System.out.println("최솟값: " + minNum);
        sc.close(); // 자원 해제
    }
}

// 피드백
// try-with-resources 블록 종료 시 sc.close() 자동 호출