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

print("\t\t\tQuantity\tPrice")
print("Chicken Noodle\t\t%d\t\tRM %.2f"%(chickennoodle_qty,chickennoodle * chickennoodle_qty))
print("Fried Rice\t\t%d\t\tRM %.2f"%(friedrice_qty,friedrice * friedrice_qty))
print("Beef Stew\t\t%d\t\tRM %.2f"%(beefstew_qty, beefstew * beefstew_qty))
print("Salad\t\t\t%d\t\tRM %.2f"%(salad_qty,salad * salad_qty))
print("Fruit\t\t\t%d\t\tRM %.2f"%(fruit_qty, fruit * fruit_qty))

finalprice = (chickennoodle*chickennoodle_qty)+(friedrice * friedrice_qty)+ (beefstew * beefstew_qty) + (salad * salad_qty) + (fruit*fruit_qty)
print ("Total price:\t\t\t\tRM %.2f" % (finalprice))
if finalprice > 100:
    discountedprice = finalprice*0.75
    print ("Price after 25%% discount:\t\tRM %.2f" % (discountedprice))
elif finalprice > 50:
    discountedprice = finalprice*0.8
    print ("Price after 20%% discount:\t\tRM %.2f" % (discountedprice))
elif finalprice > 20:
    discountedprice = finalprice*0.9
    print ("Price after 10%% discount:\t\tRM %.2f" % (discountedprice))
else:
    discountedprice = finalprice
    print ("Price after no discount:\t\tRM %.2f" % (discountedprice))
