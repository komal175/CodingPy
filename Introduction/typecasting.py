c=3.4
a="hello"
b=9
l=[6,4," "]
t=(2,4,5)
d={"1":"apple","2":6,"3":"honey"}
print(type(c),type(a),type(b),type(l),type(t),type(d))
print(d.keys())
print(d.items())

str1="i am Learning python"
print(str1.capitalize()) #first letter in capital
print(str1.upper())  #all letters in capital
print(str1.lower())  #all letters in lower


list=["hello",2,4,7,5,4,3,4]
print(list)
list[1] = 89
print(list)    #items can be changed
s=set(list)
print(s)

tup=(3,67,4,"iknow")
print(tup)

dic={}
dic["8"] =9
dic["roll no"]=2
print(dic.get("8"),dic.get("roll no")) #here naame is key and 1 is item
print(dic.items())
print(dic.values())

a1 = 5
a2 = 103
c1 = "harry"
print(str(a1) + str(a2) + c1)

