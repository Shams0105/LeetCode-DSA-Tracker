from module import myFunc
#Here it will not print the if block which is in module.py (__main__)

'''
"""
UNDERSTAND THIS USE CASE
WHY USE: if __name__ == "__main__":
-----------------------------------
Every Python file has a built-in variable called __name__.
- If you run the file directly: Python sets __name__ = "__main__"
- If you import the file into another script: Python sets __name__ = "filename"

Without this guard, any code outside functions/classes runs AUTOMATICALLY 
the exact moment another file imports it.
"""


# ==============================================================================
# USE CASE 1: Reusable Utility Module (e.g., Math/Billing Helper)
# Industry scenario: You want other team members to import your math functions,
# but if you run the file directly, you want it to run self-tests/sanity checks.
# ==============================================================================

def calculate_gst(amount: float, rate: float = 0.18) -> float:
    # Function to calculate tax on an order
    return round(amount * rate, 2)

def calculate_total(amount: float, rate: float = 0.18) -> float:
    # Function to get the final bill
    return round(amount + calculate_gst(amount, rate), 2)


if __name__ == "__main__":
    # This block ONLY runs when a developer tests this file directly in VS Code.
    # If "checkout_service.py" imports this file, this test code is IGNORED.
    print("[RUNNING LOCAL SANITY CHECKS]")
    sample_subtotal = 1000.0
    tax = calculate_gst(sample_subtotal)
    total = calculate_total(sample_subtotal)
    print(f"Subtotal: ₹{sample_subtotal} | Tax (18%): ₹{tax} | Total: ₹{total}")


# ==============================================================================
# USE CASE 2: Production Server / Entry Point (e.g., FastAPI / Flask / Bot)
# Industry scenario: Production servers (like Gunicorn/Uvicorn) import your 'app'
# object directly to manage worker processes. You only want the local dev server
# to start when you run the file manually.
# ==============================================================================

def create_application():
    # Pretend this initializes our web server or database connection
    print("Application initialized successfully.")
    return "AppInstance"

app = create_application()

def start_dev_server():
    # Starts the local development server on port 8000
    print("Starting local dev server at http://127.0.0.1:8000 ...")


if __name__ == "__main__":
    # Prevents production deployment tools from accidentally starting a 
    # redundant local server when they simply import 'app'.
    print("[DEV MODE DETECTED]")
    start_dev_server()
'''