import java.util.Scanner;

public class Eval68 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
            
            // 자릿수 곱 변수 초기화 - 값이 커질 때를 대비하여 type은 long으로
            long digitMultiple = 1;

            // while 문으로 반복하며 자릿수를 분해하며 변수에 곱한다
            while (n > 0) {
                int digit = n % 10; // 현재 자릿수 추출
                digitMultiple *= digit;
                n /= 10; // 다음 자릿수로 이동
            }

            // 결과 출력
            System.out.println("자릿수 곱: " + digitMultiple);
        }
    }
}