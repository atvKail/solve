package _4e1owek.solutions;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;

import _4e1owek.LoggingExtension;
import _4e1owek.CommonClasses.ListNode;

@ExtendWith(LoggingExtension.class)
public class ProblemN21Test {
    private ListNode toList(int[] arr) {
        ListNode dummy = new ListNode(0);
        ListNode cur = dummy;
        for (int v : arr) {
            cur.next = new ListNode(v);
            cur = cur.next;
        }
        return dummy.next;
    }

    private String toString(ListNode head) {
        StringBuilder sb = new StringBuilder();
        while (head != null) {
            sb.append(head.val);
            if (head.next != null) sb.append(",");
            head = head.next;
        }
        return sb.toString();
    }

    @Test
    public void testExample1() {
        ProblemN21 sol = new ProblemN21();
        ListNode l1 = toList(new int[]{1,2,4});
        ListNode l2 = toList(new int[]{1,3,4});
        ListNode merged = sol.mergeTwoLists(l1, l2);
        assertEquals("1,1,2,3,4,4", toString(merged));
    }

    @Test
    public void testExample2() {
        ProblemN21 sol = new ProblemN21();
        ListNode merged = sol.mergeTwoLists(null, null);
        assertEquals("", toString(merged));
    }

    @Test
    public void testExample3() {
        ProblemN21 sol = new ProblemN21();
        ListNode only = toList(new int[]{0});
        ListNode merged = sol.mergeTwoLists(null, only);
        assertEquals("0", toString(merged));
    }

    @Test
    public void testOneEmptyOneNonEmpty() {
        ProblemN21 sol = new ProblemN21();
        ListNode l1 = toList(new int[]{2,5});
        ListNode merged = sol.mergeTwoLists(l1, null);
        assertEquals("2,5", toString(merged));
    }

    @Test
    public void testAllSmaller() {
        ProblemN21 sol = new ProblemN21();
        ListNode l1 = toList(new int[]{1,2,3});
        ListNode l2 = toList(new int[]{4,5,6});
        ListNode merged = sol.mergeTwoLists(l1, l2);
        assertEquals("1,2,3,4,5,6", toString(merged));
    }

    @Test
    public void testInterleaved() {
        ProblemN21 sol = new ProblemN21();
        ListNode l1 = toList(new int[]{1,3,5});
        ListNode l2 = toList(new int[]{2,4,6});
        ListNode merged = sol.mergeTwoLists(l1, l2);
        assertEquals("1,2,3,4,5,6", toString(merged));
    }
}
