import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double heightCm = sc.nextDouble();
        double weightKg = sc.nextDouble();

        // 키를 m 로 환산해 BMI 계산.
        double heightMeter = heightCm * 0.01;
        double bmi = weightKg / (heightMeter * heightMeter);

        //       if / else if / ... / else 로 분류.
        // 결과값 저장 위해 판별 전 변수 작성
        String result  = "";

        if (bmi < 18.5){ 
            result = "저체중";
        } else if (18.5 <= bmi && bmi < 23){
            result = "정상";
        } else if (23 <= bmi && bmi < 25){
            result = "과체중";
        } else {
            result = "비만";
            
        } 
        
        // %.2f: 소수 둘째자리까지 구함
        // %s: 결과를 String으로 변환하여 출력
        System.out.printf("BMI: %.2f → %s\n", bmi, result);
        sc.close();
    }
}


// 피드백
// 조건 수정
// } else if (bmi < 23) {  // 앞 조건에서 18.5 이상임이 보장되므로 중복 조건 제거
        // result = "정상";
// } else if (bmi < 25) {  // 마찬가지로 23 이상 보장