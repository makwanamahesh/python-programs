def add(n1,n2):
    print("Addition :",n1+n2)
def sub(n1,n2):
    print("Subtraction :",n1-n2)
def mod(n1,n2):
    print("Modulation :",n1%n2)
def div(n1,n2):
    print("Division :",n1/n2)
def power(n1,n2):
    print("Addition :",n1**n2)

options={1:add,2:sub,3:mod,4:div,5:power}
print(options)
ch=0
ch=int(input("Enter Choice :- "))
       
if ch in options:
       options[ch](10,5)
       
    
    
