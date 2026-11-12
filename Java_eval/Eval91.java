import java.util.Scanner;

public class Eval91 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int mode = sc.nextInt();
            double temp = sc.nextDouble();

            // 0. 모드 판별 - mode가 1인 경우 섭씨 → 화씨 변환 
            // - else if를 사용하여 2인 경우 화씨 → 섭씨 변환
            if (mode == 1) {

                // 1-1. 이 경우 입력받은 temp가 섭씨이므로, 출력 시 temp와 f를 넣어야 함
                double f = temp * 9 / 5 + 32; // 화씨
                System.out.printf("%.1f°C = %.1f°F%n", temp, f);

            } else if (mode == 2) {

                // 1-2. 이 경우 입력받은 temp가 화씨이므로, 출력 시 temp와 c를 넣어야 함
                double c = (temp - 32) * 5 / 9;  // 섭씨
                System.out.printf("%.1f°F = %.1f°C%n", temp, c);
 
          
            } else {
                
                // 2. 1이나 2 이외의 값이 입력된 경우 오류 메시지 출력
                System.out.println("잘못된 입력입니다.");
            }
        }
    }
}


// 피드백
// 섭씨 변환식, 화씨 변환식을 메소드로 작성 - (재사용성 향상)
// 섭씨 → 화씨 변환 메서드 (재사용성 향상)
// private static double toFahrenheit(double celsius) {
//     return celsius * 9 / 5 + 32;
// }

// 화씨 → 섭씨 변환 메서드 (재사용성 향상)
// private static double toCelsius(double fahrenheit) {
//     return (fahrenheit - 32) * 5 / 9;
// }