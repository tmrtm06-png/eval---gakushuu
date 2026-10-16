import java.util.Scanner;

public class Eval45 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int multipleCount = 0; // 공배수 카운트 변수 초기화

        // 1 ~ n의 범위 내 숫자 중, 3과 5의 공배수인 숫자의 개수를 출력한다
        for (int i = 1; i <= n; i++) {
            if (i % 3 == 0 && i % 5 == 0) {
                multipleCount++;
            }
        }
        System.out.println("공배수 개수: " + multipleCount);
        sc.close(); // 자원 해제
    }
}


// 피드백
// try-with-resources로 Scanner를 선언하면 자동으로 자원이 해제된다
// try (Scanner sc = new Scanner(System.in)) {}