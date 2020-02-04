chickennoodle = 2.00
friedrice = 3.50
beefstew = 8.00
salad = 1.50
fruit = 4.50

chickennoodle_qty = int(input("Enter the quantity for chicken noodles: "))
friedrice_qty = int(input("Enter the quantity for fried rice: "))
beefstew_qty = int(input("Enter the quantity for beef stew: "))
salad_qty = int(input("Enter the quantity for salad: "))
fruit_qty = int(input("Enter the quantity for fruit: "))

discount = int(input("Enter the discount in %: "))

print("\t\t\tQuantity\tPrice")
print("Chicken Noodle\t\t%d\t\tRM %.2f"%(chickennoodle_qty,chickennoodle * chickennoodle_qty))
print("Fried Rice\t\t%d\t\tRM %.2f"%(friedrice_qty,friedrice * friedrice_qty))
print("Beef Stew\t\t%d\t\tRM %.2f"%(beefstew_qty, beefstew * beefstew_qty))
print("Salad\t\t\t%d\t\tRM %.2f"%(salad_qty,salad * salad_qty))
print("Fruit\t\t\t%d\t\tRM %.2f"%(fruit_qty, fruit * fruit_qty))

finalprice = (chickennoodle*chickennoodle_qty)+(friedrice * friedrice_qty)+ (beefstew * beefstew_qty) + (salad * salad_qty) + (fruit*fruit_qty)

print ("Total price:\t\t\t\tRM %.2f" % (finalprice))
print ("Price after %d%% discount:\t\tRM %.2f" % (discount,finalprice*(1-(discount/100))))
