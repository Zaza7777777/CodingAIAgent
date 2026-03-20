
# function tools to use in the actual code
def add(a, b): return a + b;
def subtract(a, b): return a - b;
def multiply(a, b): return a * b;

def divide(a, b):
    if b == 0:
        raise ValueError("Value cannot be divided by zero")
    return a / b

# list of tools I can use
tool_map = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}