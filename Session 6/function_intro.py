#INITIALIZE KHAI BAO
#CONTENT: PARAMETER, ARGUMENT
def greeting(name, age):
    print(f'hi, my name is {name}, I am {age} years old')

#CALL FUNCTIONS GOI HAM
greeting('Linh', 21)
greeting('Hitler', 100)

#VARIABLE SCOPE 
def add(a, b):
    total = a + b
    return total    #FRUIT_FULL FUNCTION
a = add(2,1)        #FRUIT_FULL FUNCTION
print(a)



