import java.util.Scanner;

public class Eval11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int month = sc.nextInt();
        // switch fall-through 로 31일/30일 케이스를 묶고,
        // 2 는 28일, default 는 "잘못된 월" 출력.
        switch (month) {
            case 1:
            case 3:
            case 5:
            case 7:
            case 8:
            case 10:
            case 12:
                System.out.println("31일");
                break;
            case 4:
            case 6:
            case 9:
            case 11:
                System.out.println("30일");
                break;
            case 2:
                System.out.println("28일");
                break;
            default:
                System.out.println("잘못된 월");
                break;
        }
        
        sc.close();
    }
}