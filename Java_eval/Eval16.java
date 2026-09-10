import java.util.Scanner;

public class Eval16 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // for 로 1*2*...*n 을 누적 계산. "N! = <값>" 형식으로 출력.
        //       (큰 N 에서 오버플로 방지를 위해 long 사용 권장)

        // 반복하며 입력받은 값 n의 팩토리얼을 구하는 식 작성
        // 1의 값을 가지는 num 정의, 입력받은 값을 포함하는 범위, 반복마다 num을 1씩 증가시킴
        long factorial = 1;  // 팩토리얼 변수 값 초기화: 곱셈 위해 1로
        for (int num = 1; num <= n; num++) {
             factorial *= num;  // factorial 변수에 num을 반복하여 곱한다
        }
        // 루프 바깥에서 결과 출력
        System.out.println(n + "! = " + factorial);
        sc.close();  // 자원 반환
    }
}