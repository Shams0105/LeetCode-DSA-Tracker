package Recursion;

public class PalindromeCheckRecursion {
    public static void main(String[] args) {
        String org = "aabaa";
        
        // Capture the boolean result and print it so you can see the output!
        boolean isPalindrome = checkPalindromeRecursion(org, 0, org.length() - 1);
        
        System.out.println(isPalindrome);
    }

    public static boolean checkPalindromeRecursion(String s, int start, int end) {
        // Base Case 1: If pointers meet or cross, we checked everything successfully!
        if (start >= end) {
            return true;
        }

        // Base Case 2: If characters at start and end don't match, it's NOT a palindrome
        if (s.charAt(start) != s.charAt(end)) {
            return false;
        }

        // Recursive Call: Move start forward and end backward, return their result
        return checkPalindromeRecursion(s, start + 1, end - 1);
    }
}
