"""The program takes the order, 
prints the order list, 
calculates the bill: 
total net cost, tax, tip and the total amount to be paid
"""

def order():
  meal = 0
  order_list = []
  tax = 6.75 / 100
  tip = 15.0 / 100
  order_atvice = True
  while order_atvice == True:
    order_continue = str(input("Is the order active? Y/N: "))
    if order_continue.upper() == "N":
      print ("\n")
      for o in order_list: 
        print (o)
      print ("\n")
      print("meal: %.2f $" % meal)
      tax_total = meal * tax
      print("tax: %.2f $" % tax_total)
      meal = meal + meal * tax
      tip_total = meal * tip
      print("tip: %.2f $" % tip_total)
      total = meal + meal * tip
      print("total: %.2f $" % total)
      order_active = False
      return
    elif order_continue.upper() == "Y":
      order = str(input("Add to order: \n1. Essperso 5$\n2. Cappuccino 7$\n3. Latte 10$\n4. Sacher Cake 15$ \n5. Cheesscake 10$\n6. Appelcake 12$\n"))
      amount = input("Amount of product: ")
      if not amount.isdigit():
        print ("Error. Invalid value")
      else:
        amount = int(amount)
        if order == "1":
          meal = meal + 5 * amount
          order_list.append("Essperso  5$ * %d" % amount)
        elif order =="2":
          meal = meal + 7 * amount
          order_list.append("Cappuccino 7$ * %d" % amount)
        elif order =="3":
          meal = meal + 10 * amount
          order_list.append("Latte 10$ * %d" % amount)
        elif order =="4":
          meal = meal + 15 * amount
          order_list.append("Sacher Cake 15$ * %d" % amount)
        elif order =="5":
          meal = meal + 10 * amount
          order_list.append("Cheesscake 10$ * %d" % amount)
        elif order =="6":
          meal = meal + 12 * amount
          order_list.append("Appelcake 12$ * %d" % amount)
        else:
          print ("Error. There is no such option")
    else:
      print ("Error. There is no such option")
	
    
order()