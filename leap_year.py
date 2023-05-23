print("\n\n\n\t\t\t---- Let's find out the Leap year ----\n\n\n")

year=int(input("Type Year   :     "))

if year%4==0:
    #print("leap")
    if year%100==0:
        #print("not Leap")
        if year%400==0:
            print("leap")
        else:
            print("not leap")
    else: 
        print("leap")
else:
    print("not leap")