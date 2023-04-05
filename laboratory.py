import random

nums = [random.randint(-100, 100) for _ in range(20)]

negative_sum = 0
for num in nums:
    if num < 0:
        negative_sum += num

even_sum = 0
for num in nums:
    if num % 2 == 0:
        even_sum += num

odd_sum = 0
for num in nums:
    if num % 2 != 0:
        odd_sum += num

index_mult = 1
for i in range(len(nums)):
    if i % 3 == 0:
        index_mult *= nums[i]

min_num = min(nums)
max_num = max(nums)
min_index = nums.index(min_num)
max_index = nums.index(max_num)
if min_index > max_index:
    min_index, max_index = max_index, min_index

between_mult = 1
for i in range(min_index + 1, max_index):
    between_mult *= nums[i]

    #this last command is made by gpt, sorry
positive_indices = []
for i in range(len(nums)):
    if nums[i] > 0:
        positive_indices.append(i)
if len(positive_indices) > 1:
    first_positive_index = positive_indices[0]
    last_positive_index = positive_indices[-1]
    between_sum = sum(nums[first_positive_index + 1:last_positive_index])
else:
    between_sum = 0

print("list:", nums)
print("The sum of negative numbers:", negative_sum)
print("Sum of even numbers:", even_sum)
print("The sum of odd numbers:", odd_sum)
print("The product of elements with indices that are multiples of 3:", index_mult)
print("The product of elements between the minimum and maximum element:", between_mult)
print("The sum of the elements between the first and the last positive element:", between_sum)
