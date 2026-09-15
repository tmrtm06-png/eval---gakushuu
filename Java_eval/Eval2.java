import java.util.Scanner;

public class Eval2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int age = sc.nextInt();
        // if 한 개로 age 가 18 이상일 때만 "성인입니다" 를 출력하세요.
        if (age >= 18) {
            System.out.println("성인입니다");
        }
        sc.close();  
    }
}
