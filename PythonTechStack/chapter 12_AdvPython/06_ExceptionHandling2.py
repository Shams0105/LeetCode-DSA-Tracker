def divide_numbers(a, b):
    try:
        # Attempt to divide a by b
        result = a / b
        # Print the answer if no error occurs
        print(f"Result of {a} / {b} = {result}")

    except ZeroDivisionError:
        # Runs specifically when dividing by zero (b == 0)
        print(f"Error: Cannot divide {a} by zero!")

    except TypeError:
        # Runs when data types are incompatible (e.g., dividing string by int)
        print(f"Error: Both inputs must be numbers, got {type(a).__name__} and {type(b).__name__}!")

    except Exception as e:
        # Catches all other standard runtime exceptions and prints the error message
        print(f"Unexpected error occurred: {e}")

    else:
        # Executes ONLY if the try block ran successfully without raising any exceptions
        print("Division completed successfully.")

    finally:
        # Always executes, regardless of whether an exception occurred or not
        print("--- Execution finished for this call ---\n")


# 1. Normal run (no exceptions)
divide_numbers(10, 2)

# 2. Triggers ZeroDivisionError
divide_numbers(10, 0)

# 3. Triggers TypeError
divide_numbers(10, "two")