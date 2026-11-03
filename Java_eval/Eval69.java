import java.util.Scanner;

public class Eval69 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            long n = sc.nextLong();

            // 역순 수를 구성하기 위한 변수 초기화 
            long reversed = 0;

            // while문으로 n을 자릿수로 분해하며 n의 역순을 구한다
            while (n > 0) {
                long digit = n % 10; // 현재 자릿수 추출
                reversed = reversed * 10 + digit;  // 자릿수를 한 칸 올리고 현재 자릿수를 추가
                n /= 10;             // 다음 자릿수로
            }

            // 결과 출력
            System.out.println("뒤집은 수: " + reversed);
        }
    }
}