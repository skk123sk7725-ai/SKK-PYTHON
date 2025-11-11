# dictionary in python:-  dictionary are used to store data values in key:value pairs

# they are unordered, mutable(chaneable) & don't allow duplicate keys.

# dict= {

#     "name":"skk",
#     "cgpa":8.5,
#     "marks":[98,99,100]

# }
# print(dict) 

# lets practice dictionary:-

# student={
# "name":"skk",
# "class":"3rd year",
# "college":"st aloysius institute of technology",
# "roll num :": 233400000

# }
# print(student)

# print(type(student) )
# print(isinstance(student,dict))
# print(isinstance(student,int))



# lets learn about nested dictionary:-

flower={
     
     "name1":"gudhal",
     "name2":"rose",
     "name3":"daheliya",
     "typesofrose":{
         1:"white rose",
         2:"red rose",
         3:"brown rose"
         
     },
     "name4":"gulmohar"

}
# print(flower)
# print(flower["typesofrose"][3])



# # operations on dictionary:-

# a=flower.values()
# print(flower.keys())
# print(a)

# # print(flower.items())
# print(flower["typesofrose"].items())

# print(flower["typesofrose"].get(1))
# print(flower["typesofrose"].get(3))

# flower.update({"name5":"habiscus"})
# print(flower)
# flower["typesofrose"].update({4:"black"})
# print(flower)

# flower.pop("name1")
# print(flower)

# flower["typesofrose"].pop(3)
# print(flower)


# Q1)store following words meaning in a python dictionary:-
# simple:-
wordmeaning={
    "table":"a piece of furtinure",
    "cat":"a small animal",
    "kite":"an object made of paper or polythene fly on sky with help of thread"
}
print(wordmeaning)
a=input("enter a dictionary word :")


meaning=wordmeaning.get(a)
if meaning is None:
    print("object not found ")

else:
 print(meaning)
#  short form:-
print(wordmeaning.get(a, "not found"))