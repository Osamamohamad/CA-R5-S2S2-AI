list=["AI", "ML", "Data Science"]
temp=input("Enter the index of the element you want to access: ")
list.extend([temp])
print(list)
list.remove(temp)
print(list)