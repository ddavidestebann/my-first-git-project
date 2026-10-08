import random
from statistics import median
from typing import List

 ################### Random list 
# List of random integers (after range validating)
def generate_numbers(count: int, lower: int = 1, upper: int = 100) -> List[int]:
    if not isinstance(count, int) or isinstance(count, bool):
        raise TypeError("count must be an integer") # Validation Count Number 
    if count < 0:
        raise ValueError("count cannot be negative") # Validation Count Number 
    if lower > upper:
        raise ValueError("lower must be less than or equal to upper") # Validation of limits  
    return [random.randint(lower, upper) for _ in range(count)]



# Anormal input is rejected before processing (Negative size of numbers)
try:
    generate_numbers(count=-1)
except (TypeError, ValueError) as error:
    print("Validation error captured:", error)
    

# Prevent calculations with an empty list
def require_numbers(numbers: List[int]) -> None:
    if not numbers:
        raise ValueError("The list of numbers cannot be empty")


################# Operation Functions

# Funtion for Arithmetic average of numbers
def calculate_average(numbers: List[int]) -> float:
    require_numbers(numbers)
    return sum(numbers) / len(numbers)


# Funtion to find the higher number
def find_max(numbers: List[int]) -> int:
    require_numbers(numbers)
    return max(numbers)


# Summarize metrics in one result (avg, maxi, min, median)
def summarize_numbers(numbers: List[int]) -> dict:
    require_numbers(numbers)
    return {
        "average": calculate_average(numbers),
        "maximum": find_max(numbers),
        "minimum": min(numbers),
        "median": median(numbers),
    }


# Error: Empty list .
try:
    summarize_numbers([])
except ValueError as error:
    print("Empty input rejected:", error)


# Generate correct input
trusted_numbers = generate_numbers(count=10)
# Display the list
print("List:", trusted_numbers)
#  Display its calculated summary.
print("Trusted summary:", summarize_numbers(trusted_numbers))
