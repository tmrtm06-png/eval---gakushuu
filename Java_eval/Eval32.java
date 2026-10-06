import java.util.Scanner;

public class Eval32 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
        int n = sc.nextInt();  // 반복 범위
        int numTotal = 0;  // 입력받은 숫자의 총합 변수 초기화
        
        // for 문으로 n만큼 반복하며 입력받은 숫자의 총합을 구한다 - 이후 요구 양식에 맞게 출력
        for (int i = 0; i < n; i++) {
            numTotal += sc.nextInt();
        }
        System.out.println("합계: " + numTotal);
        }
    }
}


// 피드백
// nt inputCount = sc.nextInt();  // 반복 범위 — 변수명을 inputCount 로 명확히
//             long numTotal = 0;  // 입력받은 숫자의 총합 (long 으로 오버플로우 방지)

//             // for 문으로 inputCount 만큼 반복하며 입력받은 숫자의 총합을 구한다
//             for (int i = 0; i < inputCount; i++) {
//                 numTotal += sc.nextInt();