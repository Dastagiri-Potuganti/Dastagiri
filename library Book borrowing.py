#4.Linbrary Book Borrowing System
'''borrowed = {"Alice":["Python","SQL","Python"],
	      "Bob":["Java","Python"],
   	      "Charlie":["SQL","C++","Java"],
	      "Diana":["Python","C++"]    }

students=[]
books=[]
books_count={}
max=0
max_students=[]
for x,y in borrowed.items():
    if x not in students:
        students.append(x)
    if type(y) is list:
        for j in y:
            if j not in books or  j not in books_count:
                books.append(j)
                books_count[j]=1
            else:
                books_count[j]+=1

    if len(y)>=max:
        max=len(y)
        max_students.append(x)
#1.
print("Unique Books Borrowed by all students:",books)
#2.
print("Count of each book was borrowed:",books_count)
#3.
print("Maximum Books Borrowed by:",max_students)
#4.
print("Books Borrowed by more than one student:")
for j,i in books_count.items():
    if (i)>1:
        print(j)'''
