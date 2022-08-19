list1 = ["Palavra1", "Palavra2", "Palavra3", "Palavra4"]
list2 = ["String1", 50, "String2", 100, 200]
list3 = [100, 75, 90, 150]

list1.extend(["OPA", "GENIO"])
list2.extend(["OLHA", 75])
list3.extend([19, 65, 43])

print(list2)
print(list1[len(list1)-2], list1[len(list1)-1])
print(list3[0], list3[2])
print(list2[1], list2[3])

