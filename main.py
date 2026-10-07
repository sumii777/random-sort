from random import shuffle
from random import randint

def sort(nums):
    steps = 0
    print(f"Array at start: {nums}")
    while nums != sorted(nums):
        shuffle(nums)
        steps += 1
    print(f"Sorted in {steps} steps.\n{nums}")

if __name__ == "__main__":
    sort([randint(0,100) for _ in range(5)])
