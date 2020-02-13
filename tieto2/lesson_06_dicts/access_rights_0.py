# access_right.py

symbols = {'execute': 'X', 'read': 'R', 'write': 'W'}

N = int(input("Give N: "))
file_rights = dict()

for k in range(N):
    filename, *rights = input("{}: ".format(k + 1)).split(" ")
    file_rights[filename] = set(rights)


M = int(input("Give M: "))
commands = [''] * M
filenames = [''] * M

for k in range(M):
    commands[k], filenames[k] = input("{}: ".format(k + 1)).split(" ")
        # e.g. "execute file.ext" -- always 2 words!

print("")  # just aesthetics for testing in Snakify

for command, filename in zip(commands, filenames):
    if symbols[command] in file_rights[filename]:
        print("OK")
    else:
        print("Access denied!")
