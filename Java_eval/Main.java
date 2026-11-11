import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int n = sc.nextInt();
        
            // 0. StringBuilder 작성 - 효율화
            StringBuilder sb = new StringBuilder();

            // 1. 입력받은 n만큼 반복하며 sb에 "*"을 추가
            for (int i = 0; i < n; i++) {
                sb.append("*");
            }

            // 2. 루프 종료 후 sb를 출력
            System.out.println(sb);
        }
    }
}

// 피드백
// StringBuilder 초기화 (n만큼 용량 예약으로 재할당 방지)
// → StringBuilder sb = new StringBuilder(n);