# Str-ข้อความ
str1="My name is"
str2="Setthawuth"
print(str1)
print(str2)
print(" ------------Build in Function ------------")
print("count is ")
print (str2.count ("t"))
print(str2.capitalize())
print(len(str1))
print(str2.lower())
print(str2.upper())
print(str2.strip("Rocket"))
print(str2.find("t"))
print(str1.replace("wuth","ja"))
print(str1.join("e"))
print(str2.ljust(20,"t"))
print(str2.rjust(5,"Y"))
print(str2.isdigit())

print("----------list&tuple----------")
list1=["A",20,"E",20,"I",20,"o",20,"u",20]
print(list1)
print(list1.count("A"))
tuple1=("Y",10,"O",20,"U",15)
print(tuple1.count("Y"))
print(len(list1))
print(len(tuple1))
print(list1.index("A"))
print(tuple1.index("Y"))
list1.append("earth")
print(list1)
list1.remove(20)
print(list1)
list1.pop(5)
print(list1)
list1.clear
print(list1)
a=("Fish")
b=("Fish",20)
print(a)
print(b)
print("----------------Set-------------")
set1={'L','O','V','E'}
for data in set1:
    print(data, end="\n")
print("---------------Build in Function-------------")
set2={"earth","eiei","handsome"}
set3={"Are","you","okay"}
set2.union(set3)
print(set2)
set2.intersection(set3)
print(set3)
set2.difference(set3)
print(set3)
set1.add("Ah ha")
print(set1)
set1.remove("Ah ha")
set1.clear()
print(set1)
print("------------Dictionaty Data type------------")
dict1 = {"name": "earth", "age": 25, "sex": "Male"}
dict2 = {"name": "jhon", "age": 30, "sex": "FeMale"}
print(dict1)
print(dict1["name"])
print(dict1["age"])
print(dict1["sex"])
for data in dict1:
    print(dict1[data])

len(dict1)
print(dict1)
dict1.keys()
dict1.values()
dict1.items()
dict1.update(dict2)
dict1.pop("earth")
dict1.clear()







