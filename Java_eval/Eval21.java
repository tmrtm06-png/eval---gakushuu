import java.util.Scanner;

public class Eval21 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); 
        int rows = sc.nextInt();
        int cols = sc.nextInt();
        // 중첩 for 문으로 "*"로 이뤄진 직사각형 출력
        // 바깥은 rows(세로), 안쪽은 cols(가로)
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.print("*");
            }
            System.out.println(); // 반복문 바깥에서 한 행 출력 후 줄바꿈
        }
        sc.close();
    }
}

// 피드백
// "*".repeat(cols)로 내부 루프 없이 한 행을 한 번에 생성
//            System.out.println("*".repeat(cols)); // println이 줄바꿈까지 처리