import java.util.Scanner;

public class Eval79 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int start = sc.nextInt();
            int end = sc.nextInt();
            int step = sc.nextInt();

            // StringBuilder로 문자열 조합 후 마지막에 한 번만 출력함
            StringBuilder sb = new StringBuilder();

            // start...end 범위 내의 숫자를 step씩 증가하는 반복문 작성
            for (int num = start; num <= end; num += step) {

                // 첫 숫자 앞에는 공백 없음 - 이후 숫자들의 앞에만 공백 붙임
                if (num > start) {
                    sb.append(" ");
                }
                sb.append(num);
            }

            // 결과 출력
            System.out.println(sb);
        }
    }
}

// 피드백

// 범용성을 위해 
// (num > start) → (sb.length > 0) 으로 변경 