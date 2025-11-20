# numbers = [1, 3, 5, 7, 9]
# new_numbers = []
# for number in numbers:
#     result = number * 2
#     new_numbers.append(result)
# print(new_numbers)

# new_numbers2 = [number * 2 for number in numbers]
# print(new_numbers2)

# test = [1, 2, 3]

# print([i * i for i in test])
# # [1,4,9]

# print([[i, i + 2] for i in test])
# # [[1,3],[2,4],[3,5]]

test_1 = [1, 2, 3]
test_2 = [4, 5, 6]
print([x * y for x in test_1 for y in test_2])
