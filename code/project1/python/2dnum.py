def twodnum(line = []):
    for i in range(2):
        row = []
        for j in range(3):
            row.append(3 * i + j)
        line.append(row)
    return line
    
# grid: [[0, 1, 2], [3, 4, 5]]
# grid[0]: [0, 1, 2]
# grid[0][1]: 1

if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(twodnum())
