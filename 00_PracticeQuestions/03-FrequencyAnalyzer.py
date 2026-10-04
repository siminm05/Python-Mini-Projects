'''
Frequency Analyzer

Given: nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
write a func that returns the number that occurs most frequently.
- if 2 numbers have the same frequency then return the smallest number
'''

def main():
    nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5]
    output = soln(nums)
    print(output)

def soln(nums):
    arr = []
    frequency = {}
    for i in nums:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1

    highest = 0
    most_frequent = 0
    for i in frequency:
        if frequency[i] > highest:
            highest = frequency[i]
            most_frequent = i

    for i in frequency:
        if frequency[i] == highest:
            arr.append(i)

    if len(arr) > 1:
        min = arr[0]
        for i in arr:
            if i < min:
                min = i
        return min
    else:
        return most_frequent



main()
