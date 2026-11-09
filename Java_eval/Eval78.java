import java.util.Scanner;

public class Eval78 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int lowerBound = sc.nextInt();
            int upperBound = sc.nextInt();

            // StringBuilder로 문자열 미리 조합한 뒤 마지막 한 번만 출력
            StringBuilder sb = new StringBuilder();

            // b부터 a까지 역순으로 순회
            for (int num = upperBound; num >= lowerBound; num--) {

                // 첫 숫자 앞에는 공백 없이, 이후 숫자들 앞에만 공백 추가
                if (num < upperBound) {
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
// 공백 추가 구문을 if (num < upperBound) 에서 
// 이미 내용이 있을 때만 공백을 추가하는 형태로 변경 → if (sb.length() > 0)