package Recursion;
//  Why package : Look at your VS Code sidebar on the left.
//  You created a folder named Recursion inside your dsa folder. Because your file is inside that folder, 
//  the very first line of your code must state package Recursion;. If you remove that line,
//  Java will throw a compilation error because the folder structure won't match the code declaration.


public class BasicRecursion {

    //Segmentation Fault / Stack Overflow condition
    public static void printOnes(){
        System.out.println(1 + " ");
        printOnes(); // Calls itself infinitely as base condition not mentioned


    }

    //Base condtion Specified
    public static void count(int n){
        if(n > 3){
            return;    //BASE CASE stops when n > 3
        }
        else{
            System.out.println(n);
            n+=1;
            count(n);
        }
    }


    public static void main(String[] args){
        //printOnes(); //Starts the infinite recursion (entry point of java program the main function)
        count(0); //Starts from 0
    }
    
}

