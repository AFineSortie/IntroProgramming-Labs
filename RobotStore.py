#productNames = [ "Ultrasonic range finder"
 #, "Servo motor"
 #, "Servo controller"
 #, "Microcontroller Board"
 #, "Laser range finder"
 #, "Lithium polymer battery"
 #]
#productPrices = [ 2.50, 14.99, 44.95, 34.95, 149.99, 8.99 ]
#productQuantities = [ 4, 10, 5, 7, 2, 8 ]
#def printStock():
# print()
 #print("Available Products")
# print("------------------")
# for i in range(0,len(productNames)):
# if productQuantities[i] > 0:
# print(str(i)+")",productNames[i], "$", productPrices[i])
# print()
#def main():
# cash = float(input("How much money do you have? $"))
# while cash > 0:
# printStock()
# vals = input("Enter product ID and quantity you wish to buy: ").split(" ")
# if vals[0] == "quit": break
# prodId = int(vals[0])
# count = int(vals[1])
# if productQuantities[prodId] >= count:
# if cash >= productPrices[prodId]:
# productQuantities[prodId] -= count
# cash -= productPrices[prodId] * count
# print("You purchased", count, productNames[prodId]+".")
# print("You have $", "{0:.2f}".format(cash), "remaining.")
# else:
# print("Sorry, you cannot afford that product.")
# else:
# print("Sorry, we are sold out of", productNames[prodId])
#main()

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def numStock(self, qtyWant):
        answer = self.quantity - qtyWant
        if answer >= 0:
            return True
        else:
            return False
    def totalCost(self, qtyBuy):
        price = qtyBuy * self.price
        return price
    def removeQty(self, qtyRemove):
        self.quantity = self.quantity - qtyRemove

products = [Product("Ultrasonic Range Finder", 2.50, 4)
, Product("Servo Motor", 14.99, 10)
, Product("Servo Controller", 44.95, 5)
, Product("Microcontroller Board", 34.95, 7)
, Product("Laser Range Finder", 149.99, 2)
, Product("Lithium Polymer Battery", 8.99, 8)]

def printStock():
    print("\nAvailable Products")
    print("------------------\n")
    for i in range(0, len(products)):
        if products[i].quantity > 0:
            print(str(i + 1) + ")", products[i].name, "$", products[i].price)

def main():
    cash = float(input("How much money do you have? $"))
    while cash > 0:
        printStock()

        vals = input("\nEnter the product ID and quantity you wish to buy: ").split(" ")
        if vals[0] == "quit":
            break
        prodID = int(vals[0])
        count = int(vals[1])

        if products[prodID - 1].numStock(count):
            if cash >= products[prodID - 1].totalCost(count):
                products[prodID - 1].removeQty(count)
                cash -= products[prodID - 1].price * count
                print("\nYou purchased", count, products[prodID - 1].name + ".")
                print("\nYou have $", cash, "remaining.")
            else:
                print("\nSorry, you cannot afford that product.")
        else:
            print("\nSorry we are sold out of", products[prodID - 1].name)
                

main()







        








    
        
