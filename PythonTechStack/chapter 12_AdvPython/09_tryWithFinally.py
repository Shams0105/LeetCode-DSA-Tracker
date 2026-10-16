'''
Sometimes we want to run a piece of code irrespective of try / except blocks.
In such cases we use try with finally,
where the finally block code runs no matter what happens w try or except
'''
def main():
    try:
        a = int(input("Enter a no:"))
        print(f"The no is {a}")

    except Exception as e:
        print(f'Error {e} occured')

    finally:
        print("try block contains err , still we're in finally-> finally excutes irrespective of try & except")
    #print("this will run no matter wht , but cant run if inside a function & an err occurs in above code")

    #finally block is executed always.

main()
#some might have doubt why cant we just use print statement in try except 
#cuz that runs no matter what as well
'''
But here's the catch if we try to run it inside a function without finnaly
the code terminates where the err occured doesnt execute the print 
however it does when its inside finally
'''