with open("files/data.txt") as file_r:
    print(file_r.read())


with open("files/data.txt", 'w') as file_w:
    file_w.writelines("hello")

