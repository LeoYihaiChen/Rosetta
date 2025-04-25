def is_prime_number(num: int) -> bool:
    assert num > 0, f"Expected positive number, got {num}"

    for i in range(2, int(num/2) + 1):
        if num % i == 0:
            return False

    return True

def print_prime_numbers(N):
    out = []
    for i in range(1, N):
        if is_prime_number(i):
            print(i)
            out.append(i)
    return out



if __name__ == "__main__":
    print_prime_numbers(1000)
