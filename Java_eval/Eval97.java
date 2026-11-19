import java.util.Scanner;

public class Eval97 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int inputNum;
            
            // 1. 정수 입력 -> 2. 양수(> 0) 아니면 반복 -> 3. 결과 출력
            // do-while 문으로 양수(> 0)가 들어올 때까지 반복 입력받음 
            do {
                inputNum = sc.nextInt();
            } while (inputNum <= 0); 
            
            // 결과 출력
            System.out.println("입력값: " + inputNum);   
        }
    }
}