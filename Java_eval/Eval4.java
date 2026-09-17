import java.util.Scanner;

public class Eval4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int score = sc.nextInt();
        // if / else 로 합격/불합격 출력.
        // 점수가 60점 이상인 경우 "합격", 그렇지 아닌 경우는 "불합격"
        if (score >= 60) {
            System.out.println("합격"); 
        } else {
            System.out.println("불합격");
        }
        sc.close();
    }
}
