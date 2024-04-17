num=int(input("Enter number: "))
if num==0:
    result=1
else:
    result=1
    for i in range(1, num + 1):
        result=result*i
    print("Factorial: ", result)