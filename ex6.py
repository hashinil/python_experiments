file = open('files/todos2.txt', 'r')
todos = file.read()
print(todos)
file.close()

file = open('files/todos.txt', 'r')
todos = file.readlines()
print(todos)
file.close()



