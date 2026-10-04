'''
List Statistics - No Built-ins

Given: nums = [4, 7, 2, 7, 9, 1, 4, 8, 2, 7]
Write a func that returns:
- minimum, maximum, second largest distinct value
- sum, avg
- number of unique values
- most frequent value

DO NOT USE:
min(), max(), sum(), set(), Counter(), sorted()
'''

def main():
    nums = [4, 7, 2, 7, 9, 1, 4, 8, 2, 7]
    output = soln(nums)
    print(output)

def soln(nums):
    length = len(nums)

    if length != 0:
        min, max, sum, avg, second_largest, counter = nums[0], 0, 0, 0, 0, 0
        frequency = {}
        for i in nums:
            if i > max:
                max = i
            elif i < min:
                min = i
            sum += i
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
            if  frequency[i] == 1:
                counter += 1

        for i in nums:
            if i < max and frequency[i] == 1:
                second_largest = i

        avg = sum / length
        print("min:", min, "\nmax:", max, "\n2nd max:", second_largest, "\nsum:",  sum, "\navg:", avg, "\nsecond_largest:", "unique valeus:", counter, "\nmost_frequent:",most_frequent)
        return min, max, second_largest, sum, avg, counter, most_frequent
    return "empty list"

main()
