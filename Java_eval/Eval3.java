import java.util.Scanner;

public class Eval3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();
        // if / else 로 짝수/홀수 출력.
        // number를 2로 나눈 값이 0인 경우 "짝수", 그렇지 않은 경우 "홀수"
        if (number % 2 == 0){
            System.out.println("짝수");
        } else {
            System.out.println("홀수");
        }
        sc.close();
    }
}