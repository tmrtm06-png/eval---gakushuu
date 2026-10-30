import java.util.Scanner;

public class Eval66 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            int num1 = sc.nextInt();
            int num2 = sc.nextInt();

            // 1...min(a, b)의 범위에서 순회하며, a와 b의 공약수를 공백 구분하여 한 줄로 출력
            for (int disivor = 1; disivor <= Math.min(num1, num2); disivor++) {
                if (num1 % disivor == 0 && num2 % disivor == 0) {
                    System.out.printf("%d ", disivor); // "%d "으로 공백 구분
                } 
            }
        }
    }
}


// 피드백
// import java.util.ArrayList; | ArrayList<Integer> 활용으로 공약수를 리스트에 담은 뒤 한 번에 출력
// String.join(" ", list); 사용하여 trailing space 발생 방지