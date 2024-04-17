#1.Write a Python program to find the sum of all elements in a list and handle the case where the list contains non-numeric values.
def prob1():
    li=[1,2,'Three',4,5,6,7,'Eight']
    s=0
    try:
        for i in li:
                s+=i
    except:
        print("List consist of strings")
        s=0
    finally:    
        print('sum =',s)


#2.Create a Dictionary containing the names of students and their corresponding grades. Write a program to calculate the average grade and handle the case where the Dictionary is empty.
def prob2():
    aiml={'student1':7.8,'student2':7.6,'student3':9.4,'student4':8.8,'student5':9.8}
    cse={}
    s=0
    avg=0
    ch=int(input('1.AIML\n2.CSE\nEnter choice: '))
    try:
        if ch==1:
            for i in aiml:
                s+=aiml[i]
            avg=s/len(aiml)
        else:
            for i in cse:
                s+=cse[i]
            avg=s/len(cse)
    except:
        print("EMPTY feeds in this class")
    finally:
        print(f'Average of Whole class ={avg}')
choice=int(input("1.Problem1\n2.Problem2\nEnter choice: "))
match choice:
    case 1:
        prob1()
    case 2:
        prob2()
    case _:
        print('Invalid choice!')