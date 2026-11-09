import java.util.Scanner;

public class Eval76 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            // 짝수 추적 플래그 변수 작성 - 초기값을 true로
            boolean allEven = true;

            // while문으로 n을 반복 순회
            while (n > 0) {
                int currentDigit = n % 10;
                
                // 현재 자릿수가 짝수가 아닌 경우 변수 갱신
                if (currentDigit % 2 != 0) {
                    allEven = false; // break대신 플래그 변수 갱신만으로 끝까지 순회
                }
                n /= 10;
            }

            // 결과 출력 - 삼항연산자로 간결화
            System.out.println(allEven ? "모두 짝수" : "홀수 포함");
        }
    }
}