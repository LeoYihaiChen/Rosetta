def borurline_use(num):
    from power import power
    if num <= 0:
        return 0
    if num == 1:
        return num
    return power(2, num - 1) + num


if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(borurline_use(3))
    