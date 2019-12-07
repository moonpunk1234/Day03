x=("Animal shelter program \n ==========================")
print(x.upper())

print(x.center(30))

animal =[]
x= int(input('How many would you like to keep :\t'))
print('\n')


for i in range(x):
    y= input ("Please Enter your animal :")
    print('\n')
    animal.append(y)
print("Total number of animals : %s" %(len(animal)) )

if x>1:
    print("Your animals are :")
    for i in animal:
        print(i , end= '\t')

elif x==1:
    print("Your animal is :")
    for i in animal:
        print(i , end= '\t')       

    print('\n')    
else:
    print("Sorry! No animal kept")
print('\n')  

print("Let's ID your animals :")
 




    
