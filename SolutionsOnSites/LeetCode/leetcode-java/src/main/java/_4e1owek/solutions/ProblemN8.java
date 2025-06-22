package _4e1owek.solutions;

public class ProblemN8 {
    public int myAtoi(String s) {
        if (s == null || s.isEmpty()) return 0;
        int i = 0, n = s.length();
        while (i < n && s.charAt(i) == ' ') {
            i++;
        }
        int sign = 1;
        if (i < n) {
            char c = s.charAt(i);
            if (c == '+' || c == '-') {
                if (c == '-') sign = -1;
                i++;
            }
        }
        long result = 0;
        while (i < n) {
            char c = s.charAt(i);
            if (c < '0' || c > '9') break;
            int digit = c - '0';
            result = result * 10 + digit;
            if (sign == 1 && result > Integer.MAX_VALUE) {
                return Integer.MAX_VALUE;
            }
            if (sign == -1 && -result < Integer.MIN_VALUE) {
                return Integer.MIN_VALUE;
            }
            i++;
        }
        return sign * (int) result;
    }
}