package _4e1owek.solutions;

class ProblemN9 {
    public static boolean isPalindrome(int x) {
        StringBuilder _BuildX = new StringBuilder("" + x);
        return (_BuildX.toString().equals(_BuildX.reverse().toString()));
    }
}