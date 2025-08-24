# Jayden Kong, 104547242

from tabulate import tabulate
import itertools

def get_int(prompt: str) -> int:
    """Custom user input for integers"""
    x = None
    while x is None:
        try:
            x = int(input(prompt))
        except ValueError:
            print("Please enter a valid integer")
    return x

def run_permutations(b: int, a: int = 3) -> list:
    """Run inputs a and b through all permutations of the equation"""
    ops = ["+", "-", "*"]
    actual_calculated = (a + 2 * b) - 10
    actual_str = f"(A + 2 * B) - 10"
    failing_cases = []

    # Run through all permutations against a and b
    for op1, op2, op3 in itertools.product(ops, repeat=3):
        expr = f"(A {op1} 2 {op2} B) {op3} 10"
        c = eval(f"({a} {op1} 2 {op2} {b}) {op3} 10")

        # Matching case that is not correct permutation -> add to result
        if c == actual_calculated and expr != actual_str:
            failing_cases.append([expr, a, b, c])

    return failing_cases

def print_result(result: list, headers: list = ["Program", "A", "B", "C"]) -> None:
    """Print result table"""
    if result:
        print("\nFailing B values:")
        print(tabulate(result, headers, tablefmt="grid"))
    else:
        print("\nNo failing cases detected in the given range.")

if __name__ == "__main__":
    result = []
    start = get_int("Enter start of B range: ")
    end = None

    # Ensure that range end is larger than start range
    while not end:
        end = get_int("Enter end of B range: ")
        if end < start:
            print("End should be larger or equal to start")
            end = None

    # Find failing cases in input range
    for b in range(start, end + 1):
        failing_cases = run_permutations(a=3, b=b)
        result.extend(failing_cases)

    print_result(result)