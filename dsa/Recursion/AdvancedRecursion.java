package Recursion;

public class AdvancedRecursion {

    public static int functionalRecursionSum(int n){
        if(n == 0){
            return 0 ;
        }
        return n + functionalRecursionSum(n - 1);

    }
    // 'sum' is the accumulator — carries the running total forward
    public static int parameterizedRecursionSum(int n , int current_sum){
        if(n==0){
            return current_sum;  // base case: just return what we've accumulated so far
        }

        return parameterizedRecursionSum( n - 1 ,  current_sum + n) ;

    }
    public static int factorialRecursion(int n){
        if(n==0){
            return 1;
        }
        return n * factorialRecursion(n-1);

    }
    
    public static void main(String[] args) {

         /*
        int result = functionalRecursionSum(5);   // KEY FIX: capture the returned value
        System.out.println(result);
        */


        /*
        int result = parameterizedRecursionSum(5 , 0);
        System.out.println(result);
        */


       int res = factorialRecursion(4);
       System.out.println("Factorial of n is: " +res);
        
    }

}
