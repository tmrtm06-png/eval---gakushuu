import java.util.Scanner;

public class Eval70 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();

            // n을 카피한 변수 - 원본 보존 위함 
            int firstDigit = n;

            // while문으로 두 자리 이상인 경우 계속 나누어 맨 앞 한 자리만 남긴다
            while (firstDigit >= 10) {
                firstDigit /= 10;
            }
            
            // 결과 출력
            System.out.println("맨 앞 자리: " + firstDigit);
        }
    }
}

// 피드백

// static long getFirstDigit(long n) {
//     while (n >= 10) {
//         n /= 10; 
//     }
//     return n;

// 메서드로 추출하면 재사용성과 테스트 용이성 ↑ 