import java.util.Scanner;

public class Eval71 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt(); // 현 문제의 경우 int 범위 내 값 입력이 보장된다
            int k = sc.nextInt();

            // 10 ^ k를 for 문으로 구현
            // k만큼 반복하며 뒤 k자리를 구할 때 나눠주는 변수 power 구하는 과정
            int power = 1;
            for (int i = 0; i < k; i++) {
                power *= 10;  
            }
            
            // 뒤 k자리의 숫자를 구한다
            int kDigit = n % power;

            // 결과 출력
            System.out.println("뒤 " + k + "자리: " + kDigit);
        }
    }
}


// 피드백 
// 입력값 n의 오버플로우 방지 시, n의 타입을 long으로 입력받는다
// → long n = sc.nextLong();