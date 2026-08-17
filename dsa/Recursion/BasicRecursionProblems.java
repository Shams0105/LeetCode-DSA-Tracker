package Recursion;
import java.util.Scanner;

public class BasicRecursionProblems {
    //In Java, you can only call a function inside System.out.println() (sout)
    // if that function returns a value (like a String, int, or boolean). 
    // You cannot call a function inside sout if its return type is void

    public static void main(String[] args) {
        
        //recursiveNames(1);

        /* 
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the value of N: ");
        int userLimit = sc.nextInt(); // Take input ONCE here
        
        System.out.println("Printing numbers from 1 to " + userLimit + ":");
        //Start recursion: Counter starts at 1, limit is what the user typed
        One2N(1, userLimit);
        sc.close();
        */

        /* 
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the value of N: ");
        int userLimit2 = sc.nextInt(); // Take input ONCE here
        
        System.out.println("Printing numbers from 1 to " + userLimit2 + ":");
        //Start recursion: Counter starts at 1, limit is what the user typed
        N2one(userLimit2);
        sc.close();
        */
        //BacktrackOne2N(3 );
        BacktrackN2One(0 , 5); 


    }


    //Problem 1 Print Name 5 times
     // Pass 'i' as a parameter so its updated value is carried forward
    public static void recursiveNames(int i) {
        String s = "Shams";
        
        //Using a loop statement inside a recursive base case is a major logical error.
        //Recursion (if) uses the system's call stack to repeat the execution by creating entirely new layers 
        // of memory frames.
        /*while(i < 5){
            System.out.println(s);
            recursiveNames();
        }*/

        if(i > 5 ){
            return;
        }
        System.out.println("My name is:" + s + "    Count:" + i);
        i+=1;
        recursiveNames(i);

    }

    //Problem 2 : print linearly from 1 to N
    public static void One2N(int i , int N) {
        
        if(i > N){
            return;
        }
        System.out.println(i);
         // Move to the next number by passing i + 1. 'n' stays the same!
        One2N(i+1,N);
        
    }

    //Problem 3 : print linearly from N to 1
    public static void N2one(int N){

        if(N < 1){
            return;
        }
        System.out.println(N);
         // Recursive call: Move down to the next smaller number
        N2one(N-1);


    }

    //Problem 4 : Print linearly from 1 to N with backtracking (no use of + operation)
    public static void BacktrackOne2N(int i ){
        if(i < 1){
            return;
        }
        BacktrackOne2N(i -1 ); //Recursive call
        System.out.println(i); //Here we printed after recursive call for 1 to N as...
    }
    //Problem 5 : Print linearly from N to 1 with backtracking (no use of - operation)
    public static void BacktrackN2One(int i , int N){
        if(i > N){
            return;
        }
        BacktrackN2One(i + 1, N);
        System.out.println(i);



    }




}
