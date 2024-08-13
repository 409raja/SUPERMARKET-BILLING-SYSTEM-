
class item:
    def __init__(self, item , itemName, price , quantity):
        self.item = item
        self.itemName = itemName
        self.price = price
        self.quantity = quantity
        
# create bill displays function
def display(l, cName , cAddress):
    total = 0
    print("\n\n")
    print("\t    NOW100 Retaile Store    ")
    print("\t  -------------------------   ")
    print("\n")
    print(f"Name : {cName} \t  Address : {cAddress}")
    print("\n")
    for obj in l:
        print(f"Item : {obj.item} \t  ItemName : {obj.itemName} \t  Price : {obj.price} \t Quantity : {obj.quantity} \t Rs : {obj.price * obj.quantity}") 
        print("---------------------------------------------------------------------------------------")
        total += obj.price * obj.quantity
        print("\n")
    print(f"\t\tTotal : {total}")
    print("\n")
    #print(f"Total item : {totalitem}" )
    #print("\n")
    print("\tThanks for visiting  ")
    print("\n\n")
        
        
        
 # Store object Array
list = []      
print("\n\n")
print("Hello Sir / Madam ----------") 
print("\n")
cName = input("Enter your name :   ")
cAddress = input("Enter your address :  ")
cMobile_No = input("Enter your Mobile No. :  ")
totalItems = int(input("Enter total items :   "))
print("\n")


for i in range (0, totalItems):
    id = (i+1)
    name = input('Enter item name :   ')
    price = int(input("Enter price :   "))
    quantity = int(input("Enter quantity :   "))
    print("\n")
    list.append(item(id, name , price , quantity))
    
    
# call display function

display(list, cName, cAddress)



