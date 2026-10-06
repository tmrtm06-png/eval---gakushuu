import java.util.Scanner;

public class Eval20 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int inputNum;
        int sum = 0;

        // do-while 문으로 입력받은 값이 0이 아닐 때까지 반복하며 숫자를 입력받는다
        do {
            inputNum = sc.nextInt();
            sum += inputNum;
        } while (inputNum != 0); 

        // "합계: " 문자열과 입력값의 총합을 이어붙여 출력
        System.out.println("합계: " + sum);
    }
}


// 피드백
// try-with-resources로 Scanner 자동 반납 (리소스 누수 방지)
//         try (Scanner sc = new Scanner(System.in)) {
// }