import random
print("Dice Game of Two Player Those Who Score 50 first Will Win The Game\n")
first=input("Enter First Player Name")
second=input("Enter Second Player Name")
score1=0
score2=0
player1=1
print("Press Enter to Move Your Turn")
print("********************************************************************\n")
   
while True:
    if player1==1:
        p1=input("{0} turn".format(first))
        print()
        score=random.randint(1,6)
        score1=score1+score
        print("{0} score is :{1}".format(first,score1))
        print()
        player1=2
        if score1>=50:
            print("Congrat's {0}  You Won the Game".format(first))
            break
        continue
    else:
        p2=input("{0} turn".format(second))
        print()
        sco=random.randint(1,6)
        score2=score2+sco
        print("{0} score is :{1}".format(second,score2))
        print()
        player1=1
        if score2>=50:
            print(" Congrat's {0} You won the Game".format(second))
            break
        
        
