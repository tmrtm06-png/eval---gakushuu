import java.util.Scanner;

public class Eval10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int day = sc.nextInt();

        // 1~7: 해당 요일을 '한국어 / 영어' 형식으로 출력
        // 그 외: '잘못된 입력' 출력
        switch (day) {
            case 1:
                System.out.println("월요일 / Monday");
                break;
            case 2:
                System.out.println("화요일 / Tuesday");
                break;
            case 3:
                System.out.println("수요일 / Wednesday");
                break;
            case 4:
                System.out.println("목요일 / Thursday");
                break;
            case 5:
                System.out.println("금요일 / Friday");
                break;
            case 6:
                System.out.println("토요일 / Saturday");
                break;
            case 7:
                System.out.println("일요일 / Sunday");
                break;
            default: // 범위 밖 입력 처리
                System.out.println("잘못된 입력");
                break;
        }

        sc.close();
    }
}