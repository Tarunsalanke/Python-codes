ch=input("Enter character: ")
if ch.isalpha():
    if ch.islower():
        print("LowerCase")
    else:
        print("UpperCase")
elif ch.isdigit():
    print("Numeric")
else:
    print("Special Character")