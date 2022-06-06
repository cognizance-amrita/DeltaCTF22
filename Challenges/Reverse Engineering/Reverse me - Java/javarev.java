import java.util.*;

public class javarev {
    public static void main(String args[]) {
        javarev vaultDoor = new javarev();
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter vault password: ");
        String userInput = scanner.next();
        String input = userInput.substring("deltaCTF{".length(), userInput.length() - 1);
        if (vaultDoor.checkPassword(input)) {
            System.out.println("Access granted.");
        } else {
            System.out.println("Access denied!");
        }
    }

    public boolean checkPassword(String password) {
        return password.length() == 25 &&
                password.charAt(0) == 'u' &&
                password.charAt(4) == 'r' &&
                password.charAt(2) == '5' &&
                password.charAt(23) == 'r' &&
                password.charAt(3) == 'c' &&
                password.charAt(17) == '@' &&
                password.charAt(1) == 'n' &&
                password.charAt(7) == 'b' &&
                password.charAt(10) == '_' &&
                password.charAt(5) == '@' &&
                password.charAt(9) == '3' &&
                password.charAt(11) == 't' &&
                password.charAt(15) == 'c' &&
                password.charAt(8) == 'l' &&
                password.charAt(12) == 'h' &&
                password.charAt(20) == 'c' &&
                password.charAt(14) == '_' &&
                password.charAt(6) == 'm' &&
                password.charAt(24) == '5' &&
                password.charAt(18) == 'r' &&
                password.charAt(13) == '3' &&
                password.charAt(19) == '@' &&
                password.charAt(21) == 't' &&
                password.charAt(16) == 'h' &&
                password.charAt(22) == '3';
    }
}
