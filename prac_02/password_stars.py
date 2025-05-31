minimum_length = int(input("Set Minimum Length: "))
user_password = input("Enter Password: ")
while len(user_password) < minimum_length:
	print(f"Password length must be at least {minimum_length} characters long.")
	user_password = input("Enter Password: ")
print("*" * len(user_password))