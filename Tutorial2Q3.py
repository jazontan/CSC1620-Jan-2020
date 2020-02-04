fail = 0
stuname = input("Please enter student name: ")
marks1 = float(input ("Please enter marks for Subject 1: "))
if marks1 >= 80:
    print ("Grade for Subject 1 is A")
elif marks1>= 70:
    print ("Grade for Subject 1 is B")
elif marks1 >= 60:
    print ("Grade for Subject 1 is C")
elif marks1 >= 50:
    print ("Grade for Subject 1 is D")
else:
    print ("Grade for Subject 1 is F")
    fail = fail + 1
    
marks2 = float(input ("Please enter marks for Subject 2: "))
if marks2 >= 80:
    print ("Grade for Subject 2 is A")
elif marks2 >= 70:
    print ("Grade for Subject 2 is B")
elif marks2 >= 60:
    print ("Grade for Subject 2 is C")
elif marks2 >= 50:
    print ("Grade for Subject 2 is D")
else:
    print ("Grade for Subject 2 is F")
    fail = fail + 1

marks3 = float(input ("Please enter marks for Subject 3: "))
if marks3 >= 80:
    print ("Grade for Subject 3 is A")
elif marks3 >= 70:
    print ("Grade for Subject 3 is B")
elif marks3 >= 60:
    print ("Grade for Subject 3 is C")
elif marks3 >= 50:
    print ("Grade for Subject 3 is D")
else:
    print ("Grade for Subject 3 is F")
    fail = fail + 1

marks4 = float(input ("Please enter marks for Subject 4: "))
if marks4 >= 80:
    print ("Grade for Subject 4 is A")
elif marks4 >= 70:
    print ("Grade for Subject 4 is B")
elif marks4 >= 60:
    print ("Grade for Subject 4 is C")
elif marks4 >= 50:
    print ("Grade for Subject 4 is D")
else:
    print ("Grade for Subject 4 is F")
    fail = fail + 1

marks5 = float(input ("Please enter marks for Subject 5: "))
if marks5 >= 80:
    print ("Grade for Subject 5 is A")
elif marks5>= 70:
    print ("Grade for Subject 5 is B")
elif marks5 >= 60:
    print ("Grade for Subject 5 is C")
elif marks5 >= 50:
    print ("Grade for Subject 5 is D")
else:
    print ("Grade for Subject 5 is F")
    fail = fail + 1

average = (marks1+marks2+marks3+marks4+marks5)/5
print("\nYour average is %.2f" % (average))
if average >= 80:
    print ("Average is A")
elif average >= 70:
    print ("Average is B")
elif average >= 60:
    print ("Average is C")
elif average >= 50:
    print ("Average is D")
else:
    print ("Average is F")

if fail >= 3:
    print ("You will have to repeat this semester because you have failed %d subjects" % (fail))
else:
    print ("You have passed this semester and can move on to the next semester")
