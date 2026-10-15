import java.util.Scanner;

public class Eval39 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); // 반복 범위
        int a = sc.nextInt(); // 숫자 구간 a
        int b = sc.nextInt(); // 숫자 구간 b
        int numCount = 0;
        
        // for 문으로 n번 반복하며 정수를 입력받는다
        for (int i = 0; i < n; i++) {
        int inputNum = sc.nextInt();

        // 검사하는 정수가 구간 a이상 b이하인 경우, 카운트 변수 가산
        // 두 조건 모두 충족해야 하므로 &, && 연산자 사용 
        if (a <= inputNum && inputNum <= b) {
            numCount++;
        }
        }
        System.out.println("구간 내 개수: " + numCount);
        sc.close(); // 자원 해제
    }
}

// 피드백
// 변수명 의미 명확화
// a -> lowerBound
// b -> upperBound