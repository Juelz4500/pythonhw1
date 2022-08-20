#Excercize 1 

def cubes():
    for num in range(1,1000):
        num = num * num * num
        if num==1000:
            break
        print(num)

cubes()

#Excercise 2

for num in range(1, 100):
    if num > 1:

        for i in range(2,num):
            if num%i == 0:
                break

        else:
            print("This is a prime number")
            print(num)


#Excercise 3

age = int(input('How old are you?: '))
if age<18:
    print("kids")

elif age>18 or age<65:
    print("adults")

else: 
    print("seniors")
    
print(str(age))





