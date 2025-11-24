
def save_data(friends):
    with open("friends_list.txt", "w", encoding="utf-8") as f:
        for name in friends:
            f.write(name + "\n")
    print("all data saved with successfully")