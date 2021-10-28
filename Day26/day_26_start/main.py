# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above 👆
#
# # Write your 1 line code 👇 below:
#
# squared_numbers = [n ** 2 for n in numbers]
#
# # Write your code 👆 above:
#
# print(squared_numbers)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # 🚨 Do Not Change the code above
#
# # Write your 1 line code 👇 below:
#
# result = [n for n in numbers if n % 2 == 0]
#
# # Write your code 👆 above:
#
# print(result)


with open("file1.txt") as f:
  lines = f.readlines()
  file_1 = [int(l.rstrip()) for l in lines]

with open("file2.txt") as f:
  lines = f.readlines()
  file_2 = [int(l.rstrip()) for l in lines]

result = [n for n in file_2 if n in file_1]

# Write your code above 👆

print(result)

