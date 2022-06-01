import random


options = ["R","P","S"]
print (options)

def choice(User=input("type R for rock, P for paper or S for scissors\n")):
    while True:
        user = User
        user = user.upper()

        if user not in options:
            print ("error, invalid input, try again")
            User=input("type R for rock, P for paper or S for scissors\n")
        else:
            break
    cpu = random.choice(options)
    print (f"Player ({user}) : CPU ({cpu})")
    decision(user, cpu)
    


def decision(player, comp):
    user=player
    cpu=comp
    if user==cpu:
        print (f"both players selected {user} Tie! try again")
        choice(input("type R for rock, P for paper or S for scissors\n"))
    elif user=="R":
        if cpu=="P":
            print ("cpu wins,Paper covers Rock")
        else:
            print ("Player wins, you win, Rock smshes scissors")
    elif user=="P":
        if cpu=="R":
            print ("Player wins,you win, paper covers rock")
        else:
            print ("CPU wins, Scissors cuts Paper")
    elif user=="S":
        if cpu=="R":
            print ("CPU wins, Rock smashes Scissors")
        else:
            print ("Player wins, you win, Scissors cuts Paper")    
       
choice()
   
    
    
     