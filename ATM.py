import random
x= input('Enter The Amount')
y= random.randint(0,2000)
if y in range(0,2000):
    if x%5== 0.0:
        print('Entered Input'+ x+'$')
        print('\n')
        print('Remaing Balance'+ y-x-0.5+'$')
        
    else:
        print(x +' Not a Multiple of 5')
        print('\n')
        print('Reamaininging Balance'+ y)
else: 
    print('Insuffiecint Funds')
    print('\n')
    print('Reamaining Balance'+y)
        
