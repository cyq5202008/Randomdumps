nums = [3, 0, 1]
n = len(nums)
sum1 = n * (n + 1) // 2
sum2 = sum(nums)
missing = sum1 - sum2
print(missing)