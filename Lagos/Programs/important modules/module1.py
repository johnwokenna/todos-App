import glob

""" code to list all files in the current directory"""

myfiles = glob.glob("*.txt")
print(myfiles)

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())
