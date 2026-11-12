import java.util.Scanner;

public class Eval90 {
    
    // 0. 인치를 센티미터로 변환할 때 사용되는 값을 상수 선언
    private static final double INCH_TO_CENTI = 2.54;

    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            double inch = sc.nextDouble();

            // 1. 입력받은 인치에 상수를 곱한 값을 변수에 저장
            double cm = inch * INCH_TO_CENTI;

            // 2. 결과를 출력 - 소수 둘째자리까지
            System.out.printf("%.2f cm%n", cm);
        }
    }
}