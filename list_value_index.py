fruits=["apple","banana","carrot"]
for index,value in enumerate(fruits):
    print(f"The value is {value} and index is {index}.")
fruits.append("orange")
for value in fruits:
    print(value)