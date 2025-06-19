package _4e1owek.solutions;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;
import org.junit.jupiter.api.Test;

public class ProblemN5Test {
    private final ProblemN5 sol = new ProblemN5();

    @Test
    public void testExample1() {
        String input = "babad";
        String out = sol.longestPalindrome(input);
        assertTrue(out.equals("bab") || out.equals("aba"));
    }

    @Test
    public void testExample2() {
        assertEquals("bb", sol.longestPalindrome("cbbd"));
    }

    @Test
    public void testSingleChar() {
        assertEquals("a", sol.longestPalindrome("a"));
    }

    @Test
    public void testEmpty() {
        assertEquals("", sol.longestPalindrome(""));
    }
}
