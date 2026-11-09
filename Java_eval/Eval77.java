import java.util.Scanner;

public class Eval77 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            // 입력받은 값 a에서 시작하며, b까지 +1씩 증가하는 반복문 작성
            for (int num = a; num <= b; num++) {

                // 첫 숫자의 앞에는 공백 없이, 이후의 숫자들의 앞에만 공백 붙여
                // trailing space 방지
                if (num > a) System.out.print(" ");
                System.out.print(num);
            }
            System.out.println(); // 출력의 마지막에 줄바꿈 보장
        }
    }
}

// 피드백
// StringBuilder로 문자열을 미리 조합한 뒤 마지막에 한 번만 출력함으로 효율 개선
// StringBuilder sb = new StringBuilder(); 
// → 이후 반복문 내에서 if (num > a) sb.append(' '); / sb.append(num); 으로 문자열 추가
// 마지막에 줄바꿈 보장하며 문자열 한 번 출력