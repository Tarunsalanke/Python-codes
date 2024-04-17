a,b=input("Enter two numbers").split()
a=int(a)
b=int(b)
op=input("Enter operator: ")
match op:
    case '+':
        print(a+b)
    case '-':
        print(a-b)
    case '*':
        print(a*b)
    case '/':
        print(a/b)
    case '^':
        print(a**b)
    case '%':
        print(a%b)
    case _:
        print("Invalid Operator")