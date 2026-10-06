import java.util.Scanner;

public class Eval26 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        // for 문으로 i부터 n까지의 숫자 중 짝수를 제외한 나머지 
        // 숫자를 공백 구분하여 한 줄로 출력
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0) continue;
            System.out.print(i + " ");
        }
    }
}

// 피드백
// for 문으로 1부터 n까지의 숫자 중 짝수를 제외한 나머지
        // 숫자를 공백 구분하여 한 줄로 출력
        // boolean isFirst = true; // 첫 번째 홀수 여부 추적 (앞쪽 공백 방지)
        // for (int i = 1; i <= n; i++) 
        //     if (i % 2 == 0) continue;
        //     if (!isFirst) System.out.print(" "); // 두 번째 홀수부터 앞에 공백 삽입
        //     System.out.print(i);
        //     isFirst = false;