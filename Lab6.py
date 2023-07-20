## Lab 6 - Miguel Reyes

def encode(string):
    new = ''

    for num in string:

        if (int(num) + 3) <= 9:  ## checks if the current num in encode string when added 3 is less than or equal to 9

            new = new + str((int(num) + 3))

        elif (int(num) + 3) == 12:
            new = new + str(2)
        elif (int(num) + 3) == 11:
            new = new + str(1)
        elif (int(num) + 3) == 10:
            new = new + str(0)
    return new

def decode(decoded_password):
    new = ""
    for num in new:
        # Shifting each digit down by 3 numbers to get the original digit
        original_num = (int(num) - 3) % 10
        decoded_password += str(original_num)
    return decoded_password

    

def main():
    while True:

        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n") ## Displays option menu

        option = int(input("Please enter an option: ")) ## prompts user for option input

        if option == 1:

            password = input("Please enter your password to encode: ")  ## prompts user for encode input

            print("Your password has been encoded and stored!\n")

        elif option == 2:

            decoded_password = decode(new)

            print(f"The encoded password is" , ecoded_password, "and the original password is", password.\n")

        elif option == 3:
            break

if __name__ == '__main__':
    main()
