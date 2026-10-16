import java.util.Scanner;

public class Eval43 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        int d = sc.nextInt();
        int digitCount = 0;

        // while문으로 순회하며 n % 10이 d와 같은 경우 카운터 변수 +1 증가
        // - 종료조건: n이 0보다 큰 경우
        while (n > 0) {
            if (n % 10 == d) {
                digitCount++;
            }
            n /= 10; // 다음 자릿수로 이동
        }
        System.out.println("등장 횟수: " + digitCount);
        sc.close(); // 자원 해제
    }
}

// 피드백
// 알고리즘 간결 설명
// - 나머지 연산으로 각 자릿수를 추출하는 방식 선택 (문자열 변환보다 메모리 효율적)

// int digitCount = 0; -> int occurrenceCount = 0; 
// // 서술적 이름으로 의도를 명확하게 표현