
# tuple:- a built in data type that lets us create immutable sequence of values.
# tup=(87,7,34,65,34,64,5,34,22,7,87,65,65,65)
# # tup.index() is used to know the index of present element in tuple:-
# q=tup.index(34)
# print(q)


# # tup.count is used to know the occurence of tuple element:-
# print(tup.count(65))
# print(tup.count(7))
# print(tup.count(34))

# Q)wap to ask user to enter names of their 3 frequent movies & store them in a list:-
# question if list:-
# a=input("enter your 1st favourate movie :")

# b=input("enter your 2nd favourate movie :")

# c=input("enter your 3rd favourate movie :")

# list = [a,b,c]
# print("your movie list are", list)

# Q)wap to check that a list contains a palindrome:-
list= [1,2,3,4,5]
list2=["a","b","c","b","a"]

# list.reverse()
# a=list
# print(a)

# if( list==a):{
#     print("it is palindrome")

# }
# else:{
#     print("it is not a palindrome")
# }

b=list2[::-1]
print(b)
if( list2==b):

    print("it is palindrome")


else:
    print("it is not a palindrome")
