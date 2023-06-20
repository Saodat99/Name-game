from data import data

def clean_data(data):
    cleaned = []
    for user in data:
        fixed = {}
        fixed["email"] = user["email"]
        fixed["first_name"] = user["name"].split(" ")[0]
        fixed["last_name"] = user["name"].split(" ")[1]
        fixed["date_joined"] = user["date_joined"]
        if user["admin"] == "True":
            fixed["admin"] = True
        else:
            fixed["admin"] = False
        fixed["id"] = int(user["id"])
        cleaned.append(fixed)
    return cleaned

print(clean_data(data))
