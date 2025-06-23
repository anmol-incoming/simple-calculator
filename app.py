def calc_two_num(a,b):
    op=input("choose between these sign: + , - ,*,/:")
    if op=="+" :
        return f'sum of two numbers:{a+b}'
    elif op=="-" :
        return f"sutraction of two numbers:{a-b}"
    elif op=="*" :
        return f"multiplication of two numbers:{a*b}"
    elif op=="/" :
        return f"division of two numbers:{a/b}"
    else:
        print("invalid input")
a=int(input( "enter a number:"))
b=int(input("enter another number:"))
calc=calc_two_num(a,b)
print(calc)
