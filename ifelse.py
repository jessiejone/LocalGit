num = int (input("Please input a 3 bits number:"))
if num % 2 == 0:
  print ("ou shu")
  if 4:
    print ("it's 4")
else:
  print ("ji shu")

a = num % 10
b = num //10 % 10
c = num // 100
if num == a**3 + b**3 + c**3:
  print ("yes")
else:
  print ("no")
  
'''
is, is not
in, not in
not, or, and
'''
str1 = "sunck is a good man"
str3 = "sunck is a nice man"
# string calculation
str6 = "sunck is a"
str7 = "good man"
str8 = str6 + str7
print ("str8 = ", str8)
#duplicated strings
str9 = str8 * 3
print ("str9 =", str9)
#read chacracter from string
print (str9[1])
#read a part of string
str10 = str8[6:15]
print (str10)

str11 = "sunck is a good man"
#bool
print ("good" in str11)

year = int(input("input a year"))
if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
  print ("yes")
else:
  print("no")

num = 10
str12 = "Tomorrow is another day"
f1 = 10.12345
print ("num = %d, str12 = %s, f1 = %.3f\n" % (num, str12, f1))

#eval change a string to an expression
print (eval("12+5"))

#len(str) return the length of string (charater numbers)
print (len("Hello World!"))

#lower() make string lower case upper() upper case
#swapcase make the charaters to the opposite uper or lower cases.
#capitalize() capatize the first character
#title() capatize first charater of every word
str13 = "Hello World!"
str14 = str13.lower()
print (str14)
#center(width, fillchar)
str15 = "Hello World"
print (str15.center(30, '*'))
#*********Hello World**********
#count(string[,start][,end])
str16 = "Tomorrow is nother day"
print (str16.count('is'))
