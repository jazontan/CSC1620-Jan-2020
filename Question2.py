value = int (input("Original value of the house: "))
percentage = int (input("Percentage of inflation every year: "))
year = int (input("Number of years to project: "))
print ("Year\tYear start value\tInflation rate\tYear end value")
counter = 1
while counter <= year:
  inflation = value*(percentage/100)
  print ("%d\t\t%d\t\t\t\t%d\t\t\t%d"%(counter,value,inflation,value+inflation))
  value=value+inflation
  counter+=1
  