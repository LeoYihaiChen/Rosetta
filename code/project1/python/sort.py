def bubble_sort(arr = [3, 1, 4, 2]):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]              
        print(i + 1, arr)
        
if __name__ == "__main__":
    print(f"Executing {__file__}: {__name__}")
    print(bubble_sort([3, 4, 2, 1]))