import java.util.Scanner;

public class Eval40 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // 양수, 음수 카운터 초기화
        int pos = 0;
        int neg = 0;
    
        //       0 은 어느 쪽도 증가시키지 않음.
        //       두 줄로 출력.
        for (int i = 0; i < n; i++) {
            int inputNum = sc.nextInt();

            // 입력받은 정수가 양수인 경우 양수 카운트 +1
            if (inputNum > 0) {
                pos++;
              // 음수인 경우 음수 카운트 +1
            } else if (inputNum < 0) {
                neg++;
            }
        } 
        
        // 입력값이 0인 경우 카운터 증가하지 않는다
        // 양수 카운터와 음수 카운터를 각각 두 줄로 출력
        System.out.println("양수: " + pos);
        System.out.println("음수: " + neg);
        sc.close();  // 자원 해제
    }
}


// 피드백
// 주석 습관 - pos++과 같은 자명한 로직의 주석은 생략, 비직관적인 부분에 주석 작성

// 결과 출력 코드 한 줄로 처리
// 양수·음수 카운터를 각각 두 줄로 출력
// System.out.printf("양수: %d%n음수: %d%n", pos, neg); // printf로 포맷을 한 곳에 관리