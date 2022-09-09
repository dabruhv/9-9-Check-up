import random

def monster():
    num = random.randrange(1,10)
    
    if num == 1:
        print("AHHH witch")
    elif num > 1 and num <4:
        print("bruhhhhh zombie")
    elif num >= 4 and num <= 6:
        print("OMG its sans")
    else:
        print("peter parker")
    
def average(num1,num2):
    num3 = num1 + num2
    print(num3/2)




print("Mild------------------------------------------------------")

for i in range(3, 38, 5):
    print(i, end=" ")
print()

for i in range(100, 48, -2):
    print(i, end=" ")
print()    

x=int(1)
while x != 0:
    x = int(input("gimmie number"))
    print(x*2)

print("Medium--------------------------------------")

monster()

g = int(input("gimmie 1st number"))
e = int(input("gimmie 2nd number"))
average(g,e)

