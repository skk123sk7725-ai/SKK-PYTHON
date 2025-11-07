# # lists in python
# marks=["hello","hii",56,67,"rohit",77.56]
# print(len(marks))
# print(marks)
# print(marks[4])

# # list slicing :-

# a=marks[3:5]
# print(a)
# print(marks[1:5])
# print(marks[0:])
# print(marks.index(77.56))
# print(marks[:])

# list method:-
# list=[1,"hello","hii",56,67,"rohit",77.56,"skk","shrikant"]
# list.append("chintu")
# print(list)

list2=[1,2,7,6,8,4,0,9,2,1]
# list2.sort()
list2.reverse()
print(list2)

# list2.pop(0)
# print(list2)

# list2.remove(2)
# print(list2)

# list2.insert(1,6)
# print(list2)

# list2.pop()
# print(list2)
# list2.sort()
# print()

# Q)wap to ask user to enter names of their 3 frequent movies & store them in a list:-

a=input("enter your 1st favourate movie :")

b=input("enter your 2nd favourate movie :")

c=input("enter your 3rd favourate movie :")

list = [a,b,c]
print("your movie list are", list)