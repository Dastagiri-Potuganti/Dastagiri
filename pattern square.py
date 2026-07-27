rows=int(input("ENter number of rows:"))
for i in range(0,rows):
    for j in range(0,rows):
        print(chr((i+j*rows)%26+65),end=' ')
    print()
