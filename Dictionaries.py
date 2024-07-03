Dict = {"key1": 156, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5'): 5, (0, 1): 689}
print(Dict)

print(Dict["key1"])

print(Dict[(0, 1)])

print(Dict["key4"])

Dict["Key4"] = "hi"

Dict["Key9"] = "bye"

del(Dict["Key9"])

## Get all the keys
print(Dict.keys())

## Get all the values
print(Dict.values())

## Search if they is in the dictinarie
## Returns boolean
print("Key4" in Dict)
print("Key9" in Dict)


album_sales_dict = {"Back in Black" :50, "The Bodyguard": 50, "Thriller": 65 }

print(album_sales_dict["Thriller"])

print(album_sales_dict.keys())

print(album_sales_dict.values())

inventory = {}

ProductName = "Mobile Phone"
ProductQuantity = 5
ProductPrice = 20000
ProductReleaseYear = 2020

inventory["ProductName1"] = ProductName
inventory["ProductQuantity1"] = ProductQuantity
inventory["ProductPrice1"] = ProductPrice
inventory["ProductReleaseYear1"] = ProductReleaseYear

ProductName = "Laptop"
ProductQuantity = 10
ProductPrice = 50000
ProductReleaseYear = 2023

inventory["ProductName2"] = ProductName
inventory["ProductQuantity2"] = ProductQuantity
inventory["ProductPrice2"] = ProductPrice
inventory["ProductReleaseYear2"] = ProductReleaseYear

print(inventory)

print("ProductReleaseYear1" in inventory)
print("ProductReleaseYear2" in inventory)

del(inventory["ProductReleaseYear1"])
del(inventory["ProductReleaseYear2"])

## To save they keys in a list
print(list(inventory.keys()))

inventory.update({"ProductName2": "Car"})

print(inventory)

# Clear all
inventory.clear()

print(inventory)


person = {"name": "Juan", "age": 20}

personCopy = person.copy()

print(personCopy)

personCopy2 = dict(person)

print(personCopy2)

# Convert each key and value to a list
info = list(person.items())

print(info)