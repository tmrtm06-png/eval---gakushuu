import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            // 0. 입력받은 값이 0인지 판별 - 0인 경우 "0"출력
            if (n == 0) {
                System.out.println("0");
            } else {

                // 1. 0이 아닌 경우 2진수 문자열로 변경
                String binary = "";

                // 1-1. while문으로 n이 0 보다 작아질 때까지 반복
                while (n > 0) {
                    binary = (n % 2) + binary; // 나눈 값을 binary 변수(문자열) 에 이어붙임
                    n /= 2; // 다음 비트로 이동
                }

                // 2. 결과 출력 
                System.out.println(binary);
            }
        }
    }
}

// 피드백
// StringBuilder로 한데 모아 마지막에 한 번에 출력 - 효율화
// 역순으로 추가되었으므로 binart.reverse().toString()으로 원위치, string으로 변환 후 출력