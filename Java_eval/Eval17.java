import java.util.Scanner;

public class Eval17 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        // n의 복사문과 자릿수를 세기 위한 변수 작성
        int n_copy = n;
        int count = 0;
        
        // while문으로 10으로 나눠가며 자릿수 카운트
        while (temp > 0) {
            temp /= 10;
            count++;
        }
        
        System.out.println(count + "자리");
    }
}


// 피드백
        // 원본 n을 보존하기 위해 복사본 사용
//         int nCopy = n;       // n_copy → camelCase로 변경
//         int digitCount = 0;  // count → 역할이 명확한 이름으로 변경

//         // 10으로 나눠가며 자릿수를 카운트
//         while (nCopy > 0) {
//             nCopy /= 10;
//             digitCount++;
//         }

//         System.out.println(digitCount + "자리");
//         sc.close();
//     }
// }