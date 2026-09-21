import java.util.Scanner;

public class Eval14 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int isMember = sc.nextInt();
        int amount = sc.nextInt();
        // 바깥 if : 회원인지.
        // 안쪽 if/else : 금액 10000 이상인지.
        // - 10000원 이상인 경우 10% 할인 대상, 아닌 경우 할인 대상 아님
        // 바깥 else : "회원만 할인 가능".
        if (isMember == 1) {
            
            if (amount >= 10000) {
                System.out.println("10% 할인 대상");
            } else {
                System.out.println("할인 대상 아님");
            }
            
        } else {
            System.out.println("회원만 할인 가능");
        }
        sc.close();
    }
}


// 피드백
// import java.util.Scanner;

// public class Eval14 {
//     public static void main(String[] args) {
//         Scanner sc = new Scanner(System.in);
//         int isMemberInput = sc.nextInt();
//         int amount = sc.nextInt();

//         // 바깥 if : 회원인지.
//         // 안쪽 if/else : 금액 10000 이상인지.
//         // - 10000원 이상인 경우 10% 할인 대상, 아닌 경우 할인 대상 아님
//         // 바깥 else : "회원만 할인 가능".
//         boolean isMember = (isMemberInput == 1); // int 대신 boolean으로 의미를 명확히

//         if (isMember) {
//             if (amount >= 10000) {
//                 System.out.println("10% 할인 대상");
//             } else {
//                 System.out.println("할인 대상 아님");
//             }
//         } else {
//             System.out.println("회원만 할인 가능");
//         }

//         sc.close();
//     }
// }