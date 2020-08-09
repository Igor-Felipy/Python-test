import random 

chars = "abcdefghijklmnopqrstuvwxyz0123456789"
chars_list = list(chars)

password = str(input('Enter a password : '))

guess_password = ""

while(guess_password != password):
    guess_password = random.choices(chars_list, r=len(password))

    print(str(guess_password))

    if(guess_password == list(password)):
        print("Your password is: " + str(guess_password))
        break