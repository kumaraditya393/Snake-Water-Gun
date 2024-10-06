import random

def game(comp,a):
    if comp == "S":
        if a =="S":
            print("TIE")

    if comp == "W":
        if a =="W":
            print("TIE")

    if comp == "G":
        if a =="G":
            print("TIE")

    if comp == "W":
        if a =="S":
            print("Player Won!")

    if comp == "W":
        if a =="W":
            print("Computer Won!")

    if comp == "W":
        if a =="G":
         print("Computer Won!")

    if comp == "G":
        if a =="S":
         print("Player Won!")

    if comp == "G":
        if a =="W":
         print("Computer Won!")
    if comp=="G":
         if a=="G":
          print("TIE")
            

print("**********Let,s Play Snake Water Gun*********")
t=int(input("Enter the number of chances you want to play: "))

print("Computer's Turn: Snake(S) Water(W) Gun(G) ? : ")
i=1
while (i<=t):  #LOOPING TO PLAY CONTINUE

    R=random.randint(1,3) # will return any value between 1 and 3 inclusive of both.

    if R==1:
     comp='S'
    elif R==2:
        comp='W'
    elif R==3:
        comp='G'

    print("\n")
    a=input("Players's Turn: Snake(S) Water(W) Gun(G) ?")
    print("Computer choose : ",comp)

    game(comp,a)
    i=i+1
print("Well Played!!!!")