import java.util.Scanner;

public class Eval93 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            long binary = sc.nextLong();

            // 0. 결과 출력을 위한 result 변수, 10진수 변환 시 사용되는 power 변수 선언
            long result = 0;
            long power = 1; // 오버플로우 방지 위해 long으로 초기화

            // 1. 입력받은 2진수가 0보다 작아질 때까지 반복
            while (binary > 0) {
                
                // 2. 입력받은 2진수를 power를 사용하여 10진수로 변경 후 result 변수에 가산
                result += (binary % 10) * power;
                power *= 2;
                binary /= 10; // 다음 자리수로 이동
            }

            // 3. 결과 출력
            System.out.println(result);
        }
    }
}