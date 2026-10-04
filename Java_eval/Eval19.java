import java.util.Scanner;

public class Eval19 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int inputValue;
         
        // do - while 문을 사용하여 1~100 범위 내의 값이 입력될 때까지 반복
        do {
            inputValue = sc.nextInt();
        } while (inputValue < 1 || inputValue > 100);
        
        // "입력값: " 문자열과 유효값을 연결하여 출력
        System.out.println("입력값: " + inputValue);
    }
}