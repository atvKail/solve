package _4e1owek.solutions;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

import _4e1owek.LoggingExtension;

@ExtendWith(LoggingExtension.class)
public class ProblemN8Test {
    private final ProblemN8 sol = new ProblemN8();

    @Test
    public void testExample1() {
        assertEquals(42, sol.myAtoi("42"));
    }

    @Test
    public void testExample2() {
        assertEquals(-42, sol.myAtoi("   -042"));
    }

    @Test
    public void testExample3() {
        assertEquals(1337, sol.myAtoi("1337c0d3"));
    }

    @Test
    public void testExample4() {
        assertEquals(0, sol.myAtoi("0-1"));
    }

    @Test
    public void testExample5() {
        assertEquals(0, sol.myAtoi("words and 987"));
    }

    @Test
    public void testOverflowPositive() {
        String big = "9223372036854775808";
        assertEquals(Integer.MAX_VALUE, sol.myAtoi(big));
    }

    @Test
    public void testOverflowNegative() {
        String bigNeg = "-91283472332";
        assertEquals(Integer.MIN_VALUE, sol.myAtoi(bigNeg));
    }

    @Test
    public void testOnlySign() {
        assertEquals(0, sol.myAtoi("+"));
        assertEquals(0, sol.myAtoi("-"));
    }

    @Test
    public void testEmptyAndNull() {
        assertEquals(0, sol.myAtoi(""));
        assertEquals(0, sol.myAtoi(null));
    }
}