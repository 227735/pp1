# x = person.items() 
# print(x)

# for x in thisdict.values():
#   print(x)

# for x in thisdict.keys():
#   print(x)

# for x, y in thisdict.items():
#   print(x, y)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict.pop("model") #removes the item
print(thisdict)

thisdict.popitem() #removes the last inserted item
print(thisdict)

del thisdict["year"] #removes the item with the specified key name
print(thisdict) 

thisdict.clear() #empties the dictionary
print(thisdict)