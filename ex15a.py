import glob

my_files = glob.glob("files/*.txt")
print(my_files)

for file_path in my_files:
    with open(file_path, 'r') as read_f:
        print(read_f.read().upper())