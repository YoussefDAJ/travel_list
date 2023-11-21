travel_list = input(
    "Please type the names of the contries separated by a coma: "
).split(",")
for country in travel_list:
    print(f"\n{country}\n")
    visited = input("Have you ever visited {country} befor? (yes or not) \n").lower()
    if visited == "yes":
        print("I hope you had a wonderful time \n")
    else:
        print("I hope you get to visit it soon \n")
    print("-----------")
