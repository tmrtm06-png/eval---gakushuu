import java.util.Scanner;

public class Eval6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int month = sc.nextInt();
        // if / else if 시리즈로 3, 6, 9, 12 월에만 출력. 그 외는 출력 없음.
        if (month == 3) {
            System.out.println("새 학기");
        } else if (month == 6) {
            System.out.println("여름 방학");
        } else if (month == 9) {
            System.out.println("2학기");
        } else if (month == 12) {
            System.out.println("겨울 방학");
        }
        sc.close();
    }
}