#!python3
from collections import Counter

def prime(n):
    nums = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                nums.append(i)
    return Counter(nums)


def f(n):
    nums = list(prime(n).keys())
    count = 0
    for i in range(len(nums) // 2):
        if n - nums[i] in nums:
            count += 1

    return count


print(f(10))
