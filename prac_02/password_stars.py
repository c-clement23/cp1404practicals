def main():
	minimum_length = int(input("Set Minimum Length: "))
	user_password = get_password()
	while len(user_password) < minimum_length:
		print(f"Password length must be at least {minimum_length} characters long.")
		user_password = get_password()
	print_asterisks(user_password)


def print_asterisks(user_password):
	print("*" * len(user_password))


def get_password():
	user_password = input("Enter Password: ")
	return user_password


main()