import java.util.Scanner;

public class Eval7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int month = sc.nextInt();
        // if / else if / ... / else 로 계절 또는 "잘못된 월" 출력.
        if ( month == 3 || month == 4 || month == 5) {
            System.out.println("봄"); 
        } else if ( month == 6 || month == 7 || month == 8) {
            System.out.println("여름"); 
        } else if ( month == 9 || month == 10 || month == 11) {
            System.out.println("가을"); 
        } else if ( month == 12 || month == 1 || month == 2) {
            System.out.println("겨울"); 
        } else {
            System.out.println("잘못된 월");
        }
        sc.close();
    } 
}
