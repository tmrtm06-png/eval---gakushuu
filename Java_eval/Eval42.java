import java.util.Scanner;

public class Eval42 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int startYear = sc.nextInt();
        int endYear = sc.nextInt();
        int leapYearCounter = 0;

        // for 문으로 startYear ~ endYear의 범위만큼 반복하며
        // 윤년인 경우만 카운터 +1씩 증가
        // 윤년 규칙 - 4의 배수이면서(&& 연산자) 100의 배수가 아닌 해, 또는(|| 연산자) 400의 배수인 해 
        for (int year = startYear; year <= endYear; year++) {
            if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
                leapYearCounter++;
            }
        }
        System.out.println("윤년 개수: " + leapYearCounter);
        sc.close();
    }
}


// 피드백
// 윤년 여부를 판단하는 메서드로 분리하여 재사용성 향상
// static boolean isLeapYear(int year) {
//     return (year % 4 == 0 && year % 100 != 0) || year % 400 == 0;
// }

// for (int year = startYear; year <= endYear; year++) {
//             if (isLeapYear(year)) { // 메서드 호출 
//                 leapYearCounter++;
//             }
//         }