package _4e1owek.solutions;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

import _4e1owek.LoggingExtension;

@ExtendWith(LoggingExtension.class)
public class ProblemN31Test {
    private final ProblemN31 sol = new ProblemN31();

    @Test
    public void testExample1() {
        int[] nums = {1,2,3};
        sol.nextPermutation(nums);
        assertArrayEquals(new int[]{1,3,2}, nums);
    }

    @Test
    public void testExample2() {
        int[] nums = {3,2,1};
        sol.nextPermutation(nums);
        assertArrayEquals(new int[]{1,2,3}, nums);
    }

    @Test
    public void testExample3() {
        int[] nums = {1,1,5};
        sol.nextPermutation(nums);
        assertArrayEquals(new int[]{1,5,1}, nums);
    }

    @Test
    public void testSingleElement() {
        int[] nums = {42};
        sol.nextPermutation(nums);
        assertArrayEquals(new int[]{42}, nums);
    }

    @Test
    public void testTwoElements() {
        int[] nums = {2,1};
        sol.nextPermutation(nums);
        assertArrayEquals(new int[]{1,2}, nums);
    }

    @Test
    public void testMiddleDecrease() {
        int[] nums = {1,3,2};
        sol.nextPermutation(nums);
        assertArrayEquals(new int[]{2,1,3}, nums);
    }
}
