import time

def linear_search(arr,target):
    print("\nArray:" , arr)
    print("Searching for: ",target)
    print("-" * 40)

    for i in range(len(arr)):
        print(f"Checking index {i} -> value {arr[i]}")
        time.sleep(0.7)

        if arr[i] == target:
            print(f"\n Element {target} FOUND at index {i}")
            return i

    print(f"\n Element {target} NOT FOUND")
    return -1