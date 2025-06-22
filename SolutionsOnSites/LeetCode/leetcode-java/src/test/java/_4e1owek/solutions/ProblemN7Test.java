package _4e1owek.solutions;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

import _4e1owek.LoggingExtension;

@ExtendWith(LoggingExtension.class)
public class ProblemN7Test {
    private final ProblemN7 sol = new ProblemN7();

    @Test
    public void testExample1() {
        assertEquals(321, sol.reverse(123));
    }

    @Test
    public void testExample2() {
        assertEquals(-321, sol.reverse(-123));
    }

    @Test
    public void testExample3() {
        assertEquals(21, sol.reverse(120));
    }

    @Test
    public void testZero() {
        assertEquals(0, sol.reverse(0));
    }

    @Test
    public void testNegativeWithTrailingZeros() {
        assertEquals(-21, sol.reverse(-1200));
    }

    @Test
    public void testOverflowPositive() {
        assertEquals(0, sol.reverse(1534236469));
    }

    @Test
    public void testOverflowNegative() {
        assertEquals(0, sol.reverse(-1563847412));
    }

    @Test
    public void testMaxInt() {
        assertEquals(0, sol.reverse(Integer.MAX_VALUE));
    }

    @Test
    public void testMinInt() {
        assertEquals(0, sol.reverse(Integer.MIN_VALUE));
    }
}