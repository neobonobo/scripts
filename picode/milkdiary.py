f=open("milklog.txt","w")

while True:
    customer=input("Customer name > ")
    
    if customer=="quit":
        print("Quitting...")
        break

    milk=input("How many liter for " + customer + "> ")
    f.write(customer + "bought" + milk + "liter of milk" +  "\n")
f.close()
