file = open('fsi.txt', 'w')
# r for read, w write, a append, r+ open a disk file for updating (reading and writing)
print(file.name)
print(file.mode)
print(file.writable())
file.write("this is a file")
file.close()

# read input without prompt
# when call input(), python waits for user input
x = input()
print("you enter %s,I didn't prompt you anythin" % x)
