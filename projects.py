#PROJECT_1
#snake, water, gun
import random
def win(comp, you):
    if (comp==you):
        return None
    elif comp=='s':
        if you=='w':
                return False
        elif you=='g':
                return True
    elif comp=='w':
        if you=='s':
            return True
        elif you=='g':
            return False
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True
    
        
            
n=random.randint(1,3)
if n==1:
    comp='s'
elif n==2:
    comp='w'
elif n==3:
    comp='g'
print("comp turn: choose s,w,g: ")
you=input("your turn:choose s,w,g: ")

print("comp choose: ",comp)
print("you choose: ",you)
a=win(comp, you)
if a==None:
    print("tie")
elif a:
    print("you win")
else:
    print("you loose")


#2nd projects
# import random
# comp_guess=random.randrange(1,101)
# print(comp_guess)
# player_guess=0
# gusses=0
# while(comp_guess!=player_guess):
#    player_guess=int(input("guess no: "))
#    gusses+=1
#    if comp_guess==player_guess:
#        print("you win! you guess right")
#    elif comp_guess>player_guess:
#        print("enter grater no: ")
#    elif comp_guess<player_guess:
#        print("enter smaller no: ")
# print("no of guesses:",gusses)
# OR
# import random
# comp_guess=random.randint(1,100)
# print(comp_guess)
# player_guess=0
# gusses=0
# while(comp_guess!=player_guess):
#    player_guess=int(input("guess no: "))
#    gusses+=1
#    if comp_guess==player_guess:
#        print("you win! you guess right")
#    else:
#        if comp_guess>player_guess:
#            print("enter grater no: ")
#        else:
#            print("enter smaller no: ")
# print("no of guesses:",gusses)
# with open("done.txt","r") as f:
#     compare=int(f.read())             
# if gusses<compare:
#     with open("done.txt","w") as f:   # write takes only str argument ..
#        f.write(str(gusses))           # that's why here integer converted into str..

# # if true???

     
