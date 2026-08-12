import java.util.Scanner;
public class basic_maths {
    public static void main(String[] args) { //Entry point of every java code
        
        System.out.println("-----Running Basic Maths codes------");

        
        //Java runs the code insivde psvm sequentially
        //uncomment the code u wish to run

        //runCountDigits();
        //runReverseNumber();
        //System.out.println("Is Palindrome: " + runCheckPalindrome()); //necessary for palindrome boolean return 

        //runCheckArmstrong();
        //runPrintAllDivisors();
        //isPrime();
        //System.out.println("GCD is: " + runGCD()); 
    }
    //Functions describing code for basic maths.

    //Basic trial code
    public static void runCountDigits() {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter your number to count its digits: ");
        int n = sc.nextInt();

        int count = 0;
        while(n > 0){
            count++;
            n = n / 10;
        }
        sc.close();
        System.out.println("Number of Digits are: " + count);

    
    }

    //runReverseNumber()
    public static void runReverseNumber(){
        //Cant use user ip As code crashes cuz
        //In basiCount() func u already opened a sys.in pipeline for kerboard & even if u use sc.close()
        //at the end of tht fn & it still crashes as it destroys input.
    
        int n = 7789;

        int reverse = 0 ;
        while(n > 0){
            int lastDigit = n % 10;
            reverse = (reverse * 10) + lastDigit;
            //for 2nd iteration reverse has 9, , lastDigit = 8 hence reverse = 9 * 10 + 8 = 98 
            //similarly u get 9877
            n = n/10;

        }
        System.out.println("Reverse Number is: " +reverse);
    }

    //Palindrome no
    public static boolean runCheckPalindrome(){
        int n = 121;
        int rev = 0;
        int original = n;
        while (n>0){
            int lastDigit = n % 10;
            n = n/10;
            rev = (rev * 10) + lastDigit;
        }
        if(original == rev){
            return true;
        }
        else{
            return false;
        } 
    }
    //Armstrong Number
    public static void runCheckArmstrong() {
        int n = 153;
        int temp = n;
        int original = n;

        // Step 1: Count the total number of digits (the power)
        int count = 0;
        while(temp>0){
            temp = temp/10;
            count++;
        }
        System.out.println(count);

        //Calculate the sum of digits raised to that power
        int sum = 0;
        while(n>0){
            int lastDigit = n % 10 ;
            sum = sum + (int)Math.pow(lastDigit , count);

            n = n/10;


        }
        //Check if it matches the original no
        if(sum == original){
            System.out.println("The no " +original + " is armstrong no");
        }
        else{
            System.out.println(original + "  Is not an armstrong no");
        }
    }


    //Printing all facotrs 
    public static void runPrintAllDivisors() {
        Scanner sc2 = new Scanner(System.in);
        System.out.println("Enter your no");
        int n = sc2.nextInt();
        System.out.println("Your no is " +n);
        for(int i = 1 ; i <= n ; i++){
            if(n % i == 0){
            
                System.out.println(i);
            }
        }  
        sc2.close();
    }

    //Prime no
    
     public static boolean isPrime() {
        // Edge case: Numbers less than or equal to 1 are not prime
        int n = 17;
        if (n <= 1) {
            return false;
        }

        // Check for any factors from 2 up to the square root of n (i * i <= n)
        // This is Striver's optimal O(sqrt(N)) method
        for (int i = 2; i * i <= n; i++) {
            if (n % i == 0) {
                return false; // Found a factor, so it is NOT prime
            }
        }

        return true; // No factors found, it is prime!
    }
    public static int runGCD() {
        int n1 = 20;
        int n2 = 40;
    
        for(int i = Math.min(n1,n2) ; i >= 1;i--){

            if(n1%i == 0 && n2%i == 0){
                return i;
                
            }
        }
        return 1;


        
    }

}
