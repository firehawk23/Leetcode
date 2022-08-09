// https://leetcode.com/problems/palindrome-linked-list

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode s = head;
        ListNode f = head;
        while(f!=null && f.next!=null){
            f = f.next.next;
            s = s.next;
        }
        s = reversed(s);
        f =head;
        while(s!=null){
            if(s.val!=f.val){
                return false;
            }
            s = s.next;
            f = f.next;
        }
        return true;
    }
    
    public ListNode reversed(ListNode head){
        ListNode p =null;
        while(head!=null){
            ListNode n = head.next;
            head.next=p;
            p = head;
            head = n;
        }
        return p;
    }
}