def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n-1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n-1, auxiliary, source, destination)


if __name__ == "__main__":
    n = int(input("Enter the number of disks: "))  # Number of disks
    tower_of_hanoi(n, 'A', 'B', 'C')


