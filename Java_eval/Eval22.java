import java.util.Scanner;

public class Eval22 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int start = sc.nextInt();
        int end = sc.nextInt();

        // 이중 for 문으로 구구단 출력 - 바깥 for문은 단 수, 안쪽 for문은 단 * 1...9의 곱
        for (int i = start; i <= end; i++) {
            for (int j = 1; j <= 9; j++) {
                int result = i * j;
                System.out.println(i + " x " + j + " = " + result);         
            }
            // 하나의 단이 끝난 이후 빈 줄 출력
            System.out.println();
        }
        sc.close();
    }
}


// 피드백 
// result 변수 없이 (i * j)로 직접 계산하여 간결화 가능