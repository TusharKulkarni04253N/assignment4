# assignment 4
# problem 1

# file1 = open('sample(assignment4).txt','r')
# '''
# readinglines2 = file1.readlines()
# print(readinglines2)
# (only one at a time)
# '''
# readinglines = file1.read()
# print(readinglines)

# file1.close()

# try:
#     file2 = open('non-existent.txt', 'r')
#     readinglines3 = file2.read()
#     print(readinglines3)


# except:
#     print('This file does not exist')

# finally:
#     print("You can try to creaat a new filw to save your coding")


# problem 2

file3 = open('output(assignment4).txt' , 'w')
user = input("write something here:- ")
Write_in_me = file3.write('This data is writen ' + user + "       ")

file3 = open('output(assignment4).txt' , 'a')
user = input("append something here:- ")
Append_in_me = file3.writelines('This data is appended ' + user + "       ")