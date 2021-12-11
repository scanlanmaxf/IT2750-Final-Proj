import os

private_key = "AAAAB3NzaC1yc2EAAAABJQAAAQEA5gtmTX/ZLeDqjPGQ48jdK0PjoKFkugD+Lq9uq9O2OAEcmZrpQ+qLuV7bpP822lSm8z86JSEKHtyR"
# Randomly generated encryption key

path_to_pass = "./key.txt"


# Path to the file containing the encrypted password for validation


def encrypt_char(char):
    i = 0
    new_char = ord(char)
    while i != len(private_key):
        new_char = new_char + ord(private_key[i]) + 27
        # Preforms obfuscation routine while converting to decimal ASCII

        i = i + 1

    return chr(new_char%256)


def decrypt_char(char):
    i = len(private_key)
    new_char = ord(char)

    while i != 0:
        new_char = new_char - ord(private_key[i - 1]) - 27
        # Preforms decryption routine while converting to decimal ASCII
        i = i - 1
        # print(new_char)
    return chr(new_char%256)


def save_new_password(user_input):  # Saves new password to password file
    password = ""
    i = 0
    print("Closing file")

    while i != len(user_input):
        password = password+encrypt_char(user_input[i])
        print(password)
        i = i + 1

    password_file = open(path_to_pass, "w")
    password_file.write(password)
    password_file.close()


def validate_password(user_input):
    decrypted_password = ""
    i = 0
    password_file = open(path_to_pass, "r")
    password = password_file.read()
    password_file.close()
    while i != len(user_input):
        decrypted_password =decrypted_password +  decrypt_char(password[i])
        i = i + 1
    if(decrypted_password == user_input):
        return True
    else:
        return False



if not os.path.exists(path_to_pass):  # Checks if password file can be loaded
    response = input("\nNo password database found \n\nWould you like to create a new password database?\n\n(y)es or ("
                     "n)o\n\n>>>")
    while response != "y" and response != "n":  # Checks if user input is valid
        response = input("\nPlease input y or n\n\n>>>")
    if response == "y":
        save_new_password(input("\n\nPlease enter new password \n\n>>>"))
    if response == "n":
        quit(0)

else:
    print("Please enter user password to gain access to password database")
    input_password = input("\n>>>")
    #print(validate_password(input_password))
    while not (validate_password(input_password)):
        input_password = input("\nPassword error... \n\nPlease try again \n\n>>>")
    




a = "A"
print(ord(a))
test = encrypt_char(a)
print(test)


print(decrypt_char(test))
