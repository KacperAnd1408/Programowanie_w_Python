# FileNotFoundError

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", 'w')
#     file.write("Something")
# except KeyError as error_message:
#     print(f"That key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("This is an error I made up.")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("U re not human")

bmi = weight/(height**2)
print(bmi)


