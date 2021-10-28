# FileNotFound

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("something")
# except KeyError as error_msg:
#     print(f"The key {error_msg} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / (height ** 2)

print(bmi)
