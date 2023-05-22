print("\t\t\t------Welcome to the Movie ticket price Calculator------\n")

print("#  Age<=5 then ticket price                          :  null\n")
print("#  Age >5 and Age<=30 then price                     :  150\n")
print("#  Age >30 then price                                :  200\n")



count=int(input("How many people are with you?                        :  ",))

sum=0
print()
for i in range(count):   
    Age=int(input("What is your age?                                       :  "))
    if Age <= 5:
        print("Free")
    elif Age>5 and Age<=30:
        sum+=150    
    elif Age>30:
        sum+=200
        
print("\t\t\t---Below is the food manu---\n")

print("Choice [1] ------ Small Popcorn                           : 100 Rupees")
print("Choice [2] ------ Normal Popcorn                          : 150 Rupees")
print("Choice [3] ------ Small Popcorn + Samosa                  : 150 Rupees")
print("Choice [4] ------ Small popcorn + Samosa + potato sticks  : 200 Rupees")

print()
        
choice=int(input("Would you like to have something to eat?          :   "))



if choice==1:
    sum+=100
    print(sum)
elif choice==2:
    sum+=150
elif choice==3:
    sum+=150
elif choice==4:
    sum+=200
    
    
print('Total price of the Ticket: {}'.format(sum))
        


    