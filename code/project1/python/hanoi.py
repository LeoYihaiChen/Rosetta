class HanoiStack:
    def __init__(self, name: str, num_list: list):
        self._name = name
        self._num_list: list = num_list

    def push(self, num: int):
        if len(self._num_list) > 0 and self._num_list[-1] < num:
            print(f"Failed to to push {num} to stack '{self._name}' ({self._num_list})")
            return

        self._num_list.append(num)

    def pop(self) -> int:
        if len(self._num_list) == 0:
            print("Failed to pop a number from empty stack '{self._name}'")
            return

        return self._num_list.pop()


def hanoi(source: HanoiStack, target: HanoiStack, staging: HanoiStack, N: int, func):
    # Terminate the recursion
    if N == 0:
        print("Error: trying to move 0 element!")
        return

    if N == 1:
        num = source.pop()
        target.push(num)
        print(f"Moved {num} from {source._name} to {target._name}")
        func()
        return

    # Step 1:
    # Move [1, ..., N-1] from source to staging
    hanoi(source, staging, target, N-1, func)

    # Step 2:
    # Move N from source to target
    num = source.pop()
    target.push(num)
    print(f"Moved {num} from {source._name} to {target._name}")
    func()

    # Step 3:
    # Move [1, ..., N-1] from staging to target
    hanoi(staging, target, source, N-1, func)


def play_hanoi(N: int):
    # Create a list which contains N numbers
    num_list = [i+1 for i in range(N)]
    num_list.reverse()

    A = HanoiStack("A", num_list)
    B = HanoiStack("B", [])
    C = HanoiStack("C", [])

    def print_towers():
        print(f"  {A._name}: {A._num_list}")
        print(f"  {B._name}: {B._num_list}")
        print(f"  {C._name}: {C._num_list}")

    # Expected: C will become A, and A will be empty
    hanoi(A, C, B, N, print_towers)


if __name__ == "__main__":
    play_hanoi(100)