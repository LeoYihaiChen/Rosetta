def average(numbers):
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    numbers = input("Enter a list of numbers separated by spaces: ")
    numbers = list(map(int, numbers.split()))
    print(f"The average of {numbers} is {average(numbers)}")