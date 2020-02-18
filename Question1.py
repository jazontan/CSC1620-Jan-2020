num = input ("Enter a number: ")
if num < 'A': #this line checks if something in the string is a number or string. 
  convert = float(num)
  if convert%1 != 0: #any float number modulus by 1 and returns a value has a decimal value and not purely a round number (integer). This is a trick question.
    print ("Please enter only integer input")
  else:
    #the rest of this portion is to produce the pattern as usual
    rows=1
    while rows<= int(num):
      column = rows
      while column >= 1:
        print ("*", end="")
        column -= 1
      print ("")
      rows+=1
    rows=int(num)
    while rows>1:
      column = 1
      while column <rows:
        print("*",end="")
        column += 1
      print ("")
      rows-=1
else:
  print ("Please enter only integer input")
print ("")