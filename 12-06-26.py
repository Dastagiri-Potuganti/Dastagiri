'''1.
def reverse_string(n):
    return n[::-1]
n=input("Enter a string:")
print(reverse_string(n))'''


'''2.
def fact(n):
    if n==0:
        return 1
    return n *fact(n-1)

num=int(input("Enter a number:"))
print(fact(num))'''


'''3.
def remove_dup(n):
    return list(set(n))

x=[1,2,2,3,4,4]
print(remove_dup(x))'''


'''4.
def anagram(a,b):
    if sorted(a) == sorted(b):
        return True
    else:
        return False

x='listen'
y='silent'
print(anagram(x,y))'''


'''5.
def merge(x,y):
    return list(set(x)|set(y))
x=[1,2,3]
y=[2,3,4]
print(merge(x,y))'''
