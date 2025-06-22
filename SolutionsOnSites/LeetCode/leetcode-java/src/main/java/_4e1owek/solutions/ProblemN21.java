package _4e1owek.solutions;

import _4e1owek.CommonClasses.*;

public class ProblemN21 {
    public ListNode mergeTwoLists(ListNode l1, ListNode list2) {
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (l1 != null && list2 != null) {
            if (l1.val <= list2.val) {
                tail.next = l1;
                l1 = l1.next;
            } else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }
        tail.next = (l1 != null) ? l1 : list2;
        return dummy.next;
    }
}