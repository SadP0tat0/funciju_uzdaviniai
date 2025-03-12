# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import random


def rnd_arr(depth=0, max_depth=None):
    if max_depth is None:
        max_depth = random.randint(10, 29)  # Random max depth between 10 and 29

    length = random.randint(10, 20)  # Random length for the array
    array = [random.randint(0, 10) for _ in range(length)]  # Random elements for the array

    if depth < max_depth:  # Recursion to create nested arrays
        array.append(rnd_arr(depth + 1, max_depth))

    return array


random_array = rnd_arr()
print(random_array)


def sum_per_array(arr):
    sums = []  # List to store the sum of each subarray

    # Helper function to compute the sum for each level
    def helper(subarr):
        sub_sum = 0
        for element in subarr:
            if isinstance(element, list):
                # If the element is a subarray, recursively call helper on it
                sub_sum += helper(element)
            else:
                # If it's a number, add it to the sum for this level
                sub_sum += element
        return sub_sum

    # Iterate over the main array to calculate the sum for each subarray
    for element in arr:
        if isinstance(element, list):
            # Call helper to calculate the sum of each nested subarray
            sums.append(helper(element))
        else:
            sums.append(element)

    return sums


# Example usage
random_array = rnd_arr()  # Assuming you've defined rnd_arr() as in your previous code
print("Sum per array (including subarrays):", sum_per_array(random_array))
