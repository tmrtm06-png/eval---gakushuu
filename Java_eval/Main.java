import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int target = sc.nextInt();
            int currentNum, count = 0;  // 0. 카운트 변수와 현재 숫자 변수 초기화
            
            // 1. do-while문 내에서 숫자를 입력받는다
            do {
                currentNum = sc.nextInt();

                // 2. target 여부와 상관 없이 count 변수 + 1 가산
                count++;

            } while (currentNum != target);  // target과 같아지면 종료

            // 3. 도달 문구(줄바꿈) 와 시도 횟수 출력
            System.out.println("도달\n시도 횟수: " + count);
        }
    }
}