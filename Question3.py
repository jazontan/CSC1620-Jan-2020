num1 = int (input("First number: "))
num2 = int (input("Second number: "))
sequence = int(input("Enter sequence: "))
print (num1,end=", ")
print (num2,end="")
while sequence-2 >= 1:
  print (", ",end="")
  total = num2+num1
  print (total, end="")
  num1 = num2
  num2 = total

  sequence-=1

  
