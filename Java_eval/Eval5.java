import java.util.Scanner;

public class Eval5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int score = sc.nextInt();
        // 입력받은 점수에 따라 대응하는 장학금 유형을 판별
        // - 점수가 95점 이상인 경우: "전액 장학금"
        // - 점수가 85점 이상, 95점 미만인 경우: "반액 장학금"
        // - 점수가 75점 이상, 85점 미만인 경우: "기숙사 장학금"
        // - 이외의 점수는 출력하지 않는다
        if (score >= 95) {
            System.out.println("전액 장학금");
        } else if (score >= 85) {
            System.out.println("반액 장학금");
        } else if  (score >= 75) {
            System.out.println("기숙사 장학금");
        }
        sc.close();
    }
}
