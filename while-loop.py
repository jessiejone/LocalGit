'''
while exoression:
      statement
'''
num = 1
while num <= 5:
  print(num)
  num += 1

sum = 0
num = 1
while num <= 100:
 sum += num
 num += 1
print ("sum = %d" % (sum))

str = "Tomorrow is another day"
index = 0
while index < len(str):
 print("str[%d] = %s" % (index, str[index]))
 index += 1

str1 = 'a'
#ASCII value
print(ord(str1))
str2 = chr(65)
print(str2)

num = 100
while num <= 999:
 a = num % 10
 b = num // 10 %10
 c = num //100
 if num == a**3 + b**3 +c**3:
  print (num)
 num += 1
