'''
Remove Duplicates

Given: nums = [4, 2, 7, 4, 2, 9, 7, 1]
Create remove_duplicates(nums) that returns = [4, 2, 7, 9, 1]
'''

def main():
    nums = [4, 2, 7, 4, 2, 9, 7, 1]
    output = remove_duplicates(nums)
    print(output)

def remove_duplicates(nums):
    arr = []
    for i in nums:
        if i not in arr:
            arr.append(i)

    return arr

main()
