import random as ra
while True:
    fix=ra.choice('abcdefghijklmnopqrstuvwxyz')
    i=1
    while i<=5:
        guess=input("Enter a  guess for alphabet:")
        if guess==fix:
            print("Your Guess is Correct")
            print("You Won the game")
            break
        else:
            if guess>fix:
                print("The guess is biggest:")
            else:
                print("The guess is smallest:")
        i=i+1
    else:
        print("You lost the game")
    print("The Random alphabet is :",fix)
    ag=input("Do You Want to play again(yes/no):")
    if ag=='no':
        break

print("GAME OVER")
