my_list = [1, 2, 3, 4, 5]

with open("output.txt", "w") as file:
    for i in my_list:
        file.write(str(i)+"\n")