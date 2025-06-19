package _4e1owek.solutions;

class ProblemN2 {
    static class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }

    public static ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0), firstList = l1, SecondList = l2, Current = result;
        int currVal = 0;
        while (firstList != null || SecondList != null){
            int firVal = (firstList != null) ? firstList.val : 0;
            int secVal = (SecondList != null) ? SecondList.val : 0;
            int sum = currVal + firVal + secVal;
            currVal = sum/ 10;
            Current.next = new ListNode(sum % 10);
            Current = Current.next;
            if (firstList != null) {
                firstList = firstList.next;
            }
            if (SecondList != null) {
                SecondList = SecondList.next;
            }
        }
        if (currVal > 0){
            Current.next = new ListNode(currVal);
        }
        return result.next;
    }
}