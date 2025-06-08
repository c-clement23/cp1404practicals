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

# 3) Read file and add the first 2 numbers
with open("numbers", 'r') as in_file:
    first_number = int(in_file.readline())
    second_number = int(in_file.readline())

total = first_number + second_number
print(total)

#4) Open the file and read all lines then sum
total = 0
with open("numbers", 'r') as in_file:
    for line in in_file:
        total+= int(line)

print(total)