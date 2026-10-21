import java.util.Scanner;

public class Eval48 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // int가 가질 수 있는 최댓값으로 변수를 초기화 - 최솟값 찾기 위한 변수
        int minNum = Integer.MAX_VALUE; 
        
        // 입력받은 n만큼 반복하며 숫자를 입력받는다
        for (int i = 0; i < n; i++) {
            int input = sc.nextInt();
            // 입력받은 숫자가 최솟값 변수보다 작다면. 최솟값 변수를 갱신한다
            if (input < minNum) {
                minNum = input;
            }
        }
        // 최솟값을 출력
        System.out.println("최솟값: " + minNum);
        sc.close(); // 자원 해제
    }
}

// 피드백 
// minNum 변수의 이름을 currentNum으로 변경