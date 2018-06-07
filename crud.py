action = input("welcome to our shop, what do you want (c,r,u,d) ? ").lower()

items = ["Tshirt","sweater"]

if action == "r":
    print("our items : ")
    print(*items,sep = ",")

elif action == "c":
    newitems = input("Enter new items :")
    items.append(newitems)
    print("our items : ")
    print(*items, sep = ",")

elif action == "u":
    pos = int(input("Enter new position :"))
    newitems = input("Enter new items :")
    items.insert(pos,newitems)
    print("our items : ")
    print(*items, sep=",")

elif action == "d":
    deletepos = int(input("Delete position :"))
    items.pop(deletepos-1)
    print("our items : ")
    print(*items, sep=",")





