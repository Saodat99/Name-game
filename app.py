# 1)
try:
    int("tree")
except:
    print("An error occured")

# 2)
try:
    int("15.99")
except ValueError as err:
    print(f"An Error occured: {err}")


# 3)
my_list = [1, 2, 3, 4, 5]
try:
    my_list[5]
except IndexError:
    print(f"Index out of range. Available range: 0 - {len(my_list) -1}")


# 4)
# Enter a non-number
hats = input("How many hats do you own? ")
try:
    int(hats)
except ValueError:
    print(f"You must enter an integer {ValueError}")

