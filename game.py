print("\n\n\t\t\t\t______This is ROCK-PAPER-SEIZER Game______\n")

import random

menu=["✊", "🖐", "✌"]

print("\t\t Press 0 for Rock \n\t\t Press 1 for Paper\n\t\t Press 2 for Seizer\n")

answer=int(input("\t\tWhat is your answer ? : "))

user_input=menu[answer]
print("\n\n",user_input,"\n")

rint=random.randint(1,3)

system_output=menu[rint]

print("\n",system_output,"\n\n")


if answer==0 and rint==1:
    print("You are the winner\n\n")
elif answer==0 and rint==2: 
    print("You are the winner\n\n")
elif answer==2 and rint==1:
    print("You are the winner\n\n")
elif (answer==0 and rint==0) or (answer==1 and rint==1) or (answer==2 and rint==2):
    print("Its Draw\n\n")
else: 
    print("System is the winner\n\n")
    
