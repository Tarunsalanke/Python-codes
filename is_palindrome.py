st=input("Enter string: ")
st=st.lower()
rev=st[::-1]
if st==rev:
    print("Palindrome")
else:
    print("Not Palindrome")