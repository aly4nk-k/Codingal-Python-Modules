destination = input("Hello ! Welcome to zAir booking, Where would you like to go today  ")
ticket = int(input(f"Wow ! {destination} is a amazing place to travel to. How many people will be travelling with us ?  "))
ask_again = input(f"Would you like to confirm {ticket} as the final number of people travelling with us ?  ")

if ask_again.lower() == "yes":
    print("Cant wait to see you !")
elif ask_again.lower() == "no":
    ticket = int(input("Rewrite the amount  "))
    print("Cant wait to see you !")

add = int(input("If you would like to get more tickets enter a number and it will be added to your previous number  "))
final = ticket + add
print(f"Current number of tickets : {final}")