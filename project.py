# name = input("my name:")
# age = input("your age:")
# print(name,age)

name: str =input("type your name: ")
print("hello " + name + " welcome to my game!")

should_we_play = input("Do you want to play? ").lower()
play = should_we_play == "yes"
print(play)

if should_we_play == "y" or should_we_play == "yes":
    print("we are going to play! ")
    direction = input("Do you want to go left or right? (left/right) ").lower()
    weapon = input("choose a weapon (sword/spear): ").lower()
    if direction == "left":
        print("you went left and fell of a cliff,game over,try again. ")
    elif direction == "right":
       choice = input("okay you now see a bridge,do you want to swim under it or cross it? (swim/cross)")
       if choice == "swim" or weapon == "sword":
        print("ypu got eaten by crocodile,you die, the end! ")
       else:
        print("you found the gold and you won!") 
    else:
        print("sorry not a valid reply, now you die! ")       

else:
    print("we are not playing... ")    