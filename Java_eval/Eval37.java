import java.util.Scanner;

public class Eval37 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        
        // 1~n의 범위 내에서 k의 배수의 개수를 카운트하여 결과 출력
        int count = 0;  // 배수 카운트 변수 초기화
        for (int i = 1; i <= n; i++) {
            if (i % k == 0) {
                count += 1;
            }
        }
        System.out.println(k + "의 배수 개수: " + count);
        sc.close();
    }
}



// 피드백
// count++;  // Java 관용 표현: count += 1 대신 count++ 사용