from datetime import datetime

name = input("Enter your name:")

Items="""          RICE        40/KG
          DAL         160/KG
          SUGAR       50/KG
          COLGATE     100/1PC
          WHEAT FLOUR 40/KG
          SOAP        40/1PC
          """
#DECLERATIONS
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
dictionary={"RICE":40,"DAL":160,"COLGATE":100,"WHEAT FLOUR":40,"SOAP":40,"SUGAR": 50}

option = int(input("press 1 for the list of items : "))
if option==1:
    print(Items)
else :
    print("please enter a valid number:")

for i in range(len(Items)):
    inp1=int(input("if you want buy press 1 0r 2 for exit"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your item:")
        quantity=int(input("Enter your quantity"))
        if item in dictionary.keys():
            price = quantity * (dictionary[item])
            pricelist.append((dictionary,item,quantity,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice=totalprice+gst
        else :
            print("sorry u entered item is not available right now")

    else:
        print("u entered wrong number")

    inp=input("can i generate the bill type yes or no:")
    if inp=="yes":
        pass
        if finalprice != 0:
            print(25*"$","Chandra Super Market",25*"$")
            print(28*" ","Pulivendula")
            print("Name",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ","Items",8*" ","quantity",3*" ","Price")
            for i in range(len(pricelist)):
                print(i,10*" ",ilist[i],10*" ",qlist[i],12*" ",plist[i])
            print(75*"-")
            print(50*" ","TotalAmount:",'Rs',totalprice)
            print(50*" ","GST amount",'Rs',gst)
            print(75*"-")
            print(50*" ","FinalPrice:",'Rs',finalprice)
            print(75*"-")
            print(50*" ","Thanks for Visiting")
            print(75*"-")
            print(50*" ","Visit Again")




