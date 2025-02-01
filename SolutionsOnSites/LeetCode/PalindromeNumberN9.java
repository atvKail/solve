class Solution {
    public static boolean isPalindrome(int x) {
        StringBuilder _BuildX = new StringBuilder("" + x);
        return (_BuildX.toString().equals(_BuildX.reverse().toString()));
    }
}