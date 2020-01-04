#Сколько раз встречается каждая цифра в числе
#num = int(input())
#nums = [0,0,0,0,0,0,0,0,0,0]
#while num>0:
 #   temp = num%10
 #   nums[temp]+=1
 #   num//=10

#for i in range(len(nums)):
#   print(str(i) + ": " +str(nums[i]))
#   nums+=1

#for i in nums:
#    print(i)

#a = int(input())
#m=1
#k = 1
#while (a!=0):
 #   b=a
  #  a=int(input())
   # if (a==b):
    #    k=k+1
     #   if (k>m):
      #      m=k
       # else:
        #    k=1
#print (m)

#**************************************************************************

#Максимальное количество раз встречается число
#num = int(input())
#count = 1
#mx = 0
#last=num
#while (num !=0):
#    num=int(input())
#    if(num==last):
#        count+=1
#    else:
#        if (count>mx):
#            mx=count
#        count =1
#    last = num
#print(mx)

#a = int(input())
#b = 1
#while (a>9):
#    a = a // 10
#    b=b+1
#print(b)

#****************************************************

#СОздание и заполнение массива
#for i in rangne(len(arr)):
 #   arr2[arr[i]]+=1
#mx=0
#mxindex=0
#for i in range(len(arr2)):
#    if(arr2[i]>mx):
#        mx=arr[i]
#        mxindex = i
#print(i)




#max = 0
#num = int(input())
#temp = 0
#while (num>0):
#    temp = num%10
##    if (temp>max):
 #       max=temp
 #   num = num//10
#print(max)








#import random
#number = random.randint(0,1000)

#answer = 0
#while (True):
 #   answer = int(input("Команда 1 называет число: "))
 #   if (answer==number):
  #      print("Команда 1 победила")
  #      break
  #  if (answer>number):
  #      print("Ваше число больше нашего")
  #  elif(answer<number):
  #      print("Ваше число меньше нашего")
  #  answer = int(input("Команда 2 называет число: "))
   # if (answer==number):
   #     print("Команда 2 победила")
   #     break
   # if (answer>number):
   #     print("Ваше число больше нашего")
  #  elif(answer<number):
  #      print("Ваше число меньше нашего")

#import  random
#number = random.randint(0,10)
#answer = int(input("Команда 1 вводит число"))
#k=0;
#while(answer!= number):
#    if (answer>number):
#        print("Ваше чило больше нашего")
#    elif (answer<number):
#        print("Ваше число меньше нашего")
#    answer = int(input("Команда " + str(k%2+1) + " вводит число"))
#    k += 1
#print("Команда " + str(k%2) + " победила")


#def hello(a):
#    print(a)
#    if (a>1):
#        hello(a-1)

#hello(10)


#*****************************************************
#Простейшие процедуры
o=16
def counting(b):
    x=10
    print(x+b)
    test()
    return x+b


def test():
    print("hello")
#counting(o)
print(counting(2335346))
for i in range(10):
    print(i)






