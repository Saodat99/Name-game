from data import data

def clean_data(data):
    cleaned = []
    for user in data:
        fixed = {}
        fixed["email"] = user["email"]
        fixed["first_name"] = user["name"].split(" ")[0]
        fixed["last_name"] = user["name"].split(" ")[1]
    return cleaned


print(clean_data(data))










# try:
#     int("tree")
# except:
#     print("An error occured")


# try:
#     int("15.99")
# except ValueError as err:
#     print(f"An Error occured: {err}")

# my_list = [1, 2, 3, 4, 5]
# try:
#     my_list[5]
# except IndexError:
#     print(f"Index out of range. Available range: 0 - {len(my_list) - 1}")

# hats = input("How many hats do you own?  ")
# try:
#     int(hats)
# except ValueError:
#     print(f"You must enter an integer.")