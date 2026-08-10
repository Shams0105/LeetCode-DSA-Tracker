import java.util.Scanner;
public class basic_maths {
    public static void main(String[] args) { //Entry point of every java code
        
        System.out.println("-----Running Basic Maths codes------");
        System.out.println("Is Palindrome: " + runCheckPalindrome()); //necessary for palindrome boolean return 

        //Java runs the code insivde psvm sequentially
        //uncomment the code u wish to run

        //runCountDigits();
        //runReverseNumber();
        //runCheckPalindrome();

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
    //


}
