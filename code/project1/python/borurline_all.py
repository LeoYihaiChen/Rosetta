def borurline_all(num):
    from borurline_use import borurline_use
    out = []
    for i in range(num):
        out.append(borurline_use(i))
    return out

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(borurline_all(100))