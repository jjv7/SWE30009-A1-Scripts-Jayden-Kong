# Jayden Kong, 104547242

from tabulate import tabulate
import itertools

# ANSI colour codes
BOLD = "\033[1m"
GREEN = "\033[92m"
END = "\033[0m"

def get_int(prompt: str) -> int:
    """Custom user input for integers"""
    x = None
    while x is None:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Please enter a valid integer")
    return x

def run_permutations(a: int, b: int) -> list:
    """Run inputs a and b through all permutations of the equation"""
    ops = ["+", "-", "*"]
    actual = (a + 2 * b) - 10

    results = []

    # Run through all permutations against a and b
    for i, [op1, op2, op3] in enumerate(itertools.product(ops, repeat=3)):
        CASE = i + 1
        c = eval(f"({a} {op1} 2 {op2} {b}) {op3} 10")

        # If matching case -> highlight in bold and green
        if c == actual:
            results.append([
                f"{BOLD}{GREEN}{CASE}{END}",
                f"{BOLD}{GREEN}(A {op1} 2 {op2} B) {op3} 10{END}",
                f"{BOLD}{GREEN}{a}{END}",
                f"{BOLD}{GREEN}{b}{END}",
                f"{BOLD}{GREEN}{c}{END}"])
        else:
            results.append([CASE, f"(A {op1} 2 {op2} B) {op3} 10", a, b, c])

    return results

def print_result(result: list, headers: list = ["Case", "Program", "A", "B", "C"]) -> None:
    """Print result table"""
    print(f"\nPermutation results: ")
    print(tabulate(result, headers, tablefmt="grid"))

if __name__ == "__main__":
    a = get_int("Enter the value of a: ")
    b = get_int("Enter the value of b: ")
    result = run_permutations(a, b)
    print_result(result)