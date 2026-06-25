user_names=[]
user_phn_no=[]
user_bill=[]
u_n=input("Enter Customer name")
user_names.append(u_n)
while True:
    phn=int(input("Enter Customer phone number:"))
    cnt=0
    while phn>0:
        phn//=10
        cnt=cnt+1
    if cnt==10:
        break
    else:
        print("Enter Correct number")
user_phn_no.append(phn)
