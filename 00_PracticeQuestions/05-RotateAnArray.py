'''
Rotate an Array

Given: nums = [1, 2, 3, 4, 5]  k = 2
write a func that returns [4, 5, 1, 2, 3]

Do not use pop() repeatedly
'''

def main():
    nums = [1, 2, 3, 4, 5]
    k = 2
    output = soln(nums, k)
    print(output)

def soln(nums, k):
    arr = []
    for i in range(k+1, len(nums)):
        arr.append(nums[i])

    for i in range(k+1):
        arr.append(nums[i])

    return arr

main()
