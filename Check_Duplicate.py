def check_and_add(value, my_list):
    if value in my_list:
        print("Duplicate:", value)
    else:
        my_list.append(value)
        print("Added:", value)

my_list = []

while True:
    value = input("Enter a value (press enter to stop): ")
    if value == "":
        break
    check_and_add(value, my_list)

print("Final list:", my_list)
