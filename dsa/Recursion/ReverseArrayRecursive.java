package Recursion;
import java.util.Scanner;
import java.util.Arrays;

public class ReverseArrayRecursive {

    // Recursive function to reverse the array in place
    public static void reverseRecursive(int[] arr, int start, int end) {
        // Base Case: Stop when pointers cross or meet in the middle
        if (start >= end) {
            return;
        }

        // 1. Swap elements at start and end indices
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        // 2. Recursive call: Increment start and decrement end
        reverseRecursive(arr, start + 1, end - 1);
    }

    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        // 1. Take array size input
        System.out.print("Enter the size of the array: ");
        int size = sc.nextInt();

        int[] nums = new int[size];

        // 2. Take array elements input
        System.out.println("Enter " + size + " elements:");
        for (int i = 0; i < size; i++) {
            nums[i] = sc.nextInt();
        }

        System.out.println("Original Array: " + Arrays.toString(nums));

        // 3. Call the recursive function (start index = 0, end index = size - 1)
        reverseRecursive(nums, 0, nums.length - 1);

        // 4. Print the reversed array
        System.out.println("Reversed Array: " + Arrays.toString(nums));

        sc.close();
    }
}
