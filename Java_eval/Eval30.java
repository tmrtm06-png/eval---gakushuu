import java.util.Scanner;

public class Eval30 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int digTotal = 0; // 자릿수 총합 변수 초기화
        int t = n; // n의 값 보존 위해 복사

        while (t > 0) {
            digTotal += t % 10;  // 10으로 t를 나눈 값을 자릿수 총합 변수에 가산
            t /= 10;  // 10으로 나눠 다음 자리로
        }
        System.out.println("자릿수 합: " + digTotal);
        sc.close();
    }
}


// 피드백
// int remaining = n; // n의 값 보존 위해 복사 (remaining: 아직 처리할 남은 수)

//         while (remaining > 0) {
//             digTotal += remaining % 10;  // 1의 자리(나머지)를 총합에 가산
//             remaining /= 10;            // 다음 자리로 이동
//         }