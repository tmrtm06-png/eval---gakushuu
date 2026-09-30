import java.util.Scanner;

public class Eval12 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int day = sc.nextInt();
        // switch fall-through 로 1~5 를 "평일", 6~7 을 "주말" 로 묶어 출력.
        switch (day) {
            case 1:
            case 2:
            case 3:
            case 4:
            case 5:
                System.out.println("평일");
                break;
            case 6:
            case 7:
                System.out.println("주말");
                break;
            default:
                System.out.println("잘못된 입력");
                break;
        }
        sc.close();
    }
}


// 피드백
// default case의 마지막 break는 생략 가능
// 자신만의 언어로 주석 작성 - 간결한 알고리즘 설명과 함께