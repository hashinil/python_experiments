def get_todos(filepath='files/todos.txt'):
    """ Read Todos """
    with open(filepath, 'r') as file_read:
        todos_local = file_read.readlines()
    return todos_local


# print(__name__)
if __name__ == "__main__":
    print("hello")
    print(get_todos())