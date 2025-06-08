# 1) Open and Close file after writing
name = input("Enter your name: ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# 2) Open and read the previous saved text file and output it
in_file = open("name.txt", 'r')
name = in_file.read().strip()
in_file.close()
print(f"Hi {name}!")